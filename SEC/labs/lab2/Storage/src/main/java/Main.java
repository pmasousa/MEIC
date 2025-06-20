import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import org.apache.tuweni.bytes.Bytes;

import org.apache.tuweni.units.bigints.UInt256;
import org.hyperledger.besu.datatypes.Address;
import org.hyperledger.besu.datatypes.Wei;
import org.hyperledger.besu.evm.*;
import org.hyperledger.besu.evm.account.MutableAccount;
import org.hyperledger.besu.evm.fluent.EVMExecutor;
import org.hyperledger.besu.evm.fluent.SimpleWorld;
import org.hyperledger.besu.evm.tracing.StandardJsonTracer;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.math.BigInteger;

import org.web3j.crypto.Hash;
import org.web3j.utils.Numeric;

public class Main {

    public static void main(String[] args) {
        SimpleWorld simpleWorld = new SimpleWorld();

        Address senderAddress = Address.fromHexString("deadbeefdeadbeefdeadbeefdeadbeefdeadbeef");
        simpleWorld.createAccount(senderAddress,0, Wei.fromEth(100));
        MutableAccount senderAccount = (MutableAccount) simpleWorld.get(senderAddress);
        System.out.println("Sender Account");
        System.out.println("  Address: "+senderAccount.getAddress());
        System.out.println("  Balance: "+senderAccount.getBalance());
        System.out.println("  Nonce: "+senderAccount.getNonce());
        System.out.println();

        Address contractAddress = Address.fromHexString("1234567891234567891234567891234567891234");
        simpleWorld.createAccount(contractAddress,0, Wei.fromEth(0));
        MutableAccount contractAccount = (MutableAccount) simpleWorld.get(contractAddress);
        System.out.println("Contract Account");
        System.out.println("  Address: "+contractAccount.getAddress());
        System.out.println("  Balance: "+contractAccount.getBalance());
        System.out.println("  Nonce: "+contractAccount.getNonce());
        System.out.println("  Storage:");
        System.out.println("    Slot 0: "+simpleWorld.get(contractAddress).getStorageValue(UInt256.valueOf(0)));
        String paddedAddress = padHexStringTo256Bit(senderAddress.toHexString());
        String stateVariableIndex = convertIntegerToHex256Bit(1);
        String storageSlotMapping = Numeric.toHexStringNoPrefix(Hash.sha3(Numeric.hexStringToByteArray(paddedAddress + stateVariableIndex)));
        System.out.println("    Slot SHA3[msg.sender||1] (mapping): "+simpleWorld.get(contractAddress).getStorageValue(UInt256.fromHexString(storageSlotMapping)));
        System.out.println();

        ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
        PrintStream printStream = new PrintStream(byteArrayOutputStream);
        StandardJsonTracer tracer = new StandardJsonTracer(printStream, true, true, true, true);

        var executor = EVMExecutor.evm(EvmSpecVersion.CANCUN);
        executor.tracer(tracer);
        executor.code(Bytes.fromHexString("<INSERT_EVM_BYTECODE_HERE>"));
        executor.sender(senderAddress);
        executor.receiver(contractAddress);
        executor.worldUpdater(simpleWorld.updater());
        executor.commitWorldState();

        executor.callData(Bytes.fromHexString("f1351b93"));
        executor.execute();
        int count = extractIntegerFromReturnData(byteArrayOutputStream);
        System.out.println("Output of 'retrieve_count():' " + Integer.toString(count));

        executor.callData(Bytes.fromHexString("ef48e0bd"));
        executor.execute();
        int number = extractIntegerFromReturnData(byteArrayOutputStream);
        System.out.println("Output of 'retrieve_number():' " + Integer.toString(number));

        executor.callData(Bytes.fromHexString("82ab890a" + convertIntegerToHex256Bit(42))); // update(42)
        executor.execute();

        executor.callData(Bytes.fromHexString("f1351b93"));
        executor.execute();
        count = extractIntegerFromReturnData(byteArrayOutputStream);
        System.out.println("Output of 'retrieve_count():' " + Integer.toString(count));

        executor.callData(Bytes.fromHexString("ef48e0bd"));
        executor.execute();
        number = extractIntegerFromReturnData(byteArrayOutputStream);
        System.out.println("Output of 'retrieve_number():' " + Integer.toString(number));

        System.out.println();
        System.out.println("Sender Account");
        System.out.println("  Address: "+senderAccount.getAddress());
        System.out.println("  Balance: "+senderAccount.getBalance());
        System.out.println("  Nonce: "+senderAccount.getNonce());
        System.out.println();

        System.out.println("Contract Account");
        System.out.println("  Address: "+contractAccount.getAddress());
        System.out.println("  Balance: "+contractAccount.getBalance());
        System.out.println("  Nonce: "+contractAccount.getNonce());
        System.out.println("  Storage:");
        System.out.println("    Slot 0 (count): "+simpleWorld.get(contractAddress).getStorageValue(UInt256.valueOf(0)));
        System.out.println("    Slot SHA3[msg.sender||1] (mapping): "+simpleWorld.get(contractAddress).getStorageValue(UInt256.fromHexString(storageSlotMapping)));
    }

    public static int extractIntegerFromReturnData(ByteArrayOutputStream byteArrayOutputStream) {
        String[] lines = byteArrayOutputStream.toString().split("\\r?\\n");
        JsonObject jsonObject = JsonParser.parseString(lines[lines.length - 1]).getAsJsonObject();

        String memory = jsonObject.get("memory").getAsString();

        JsonArray stack = jsonObject.get("stack").getAsJsonArray();
        int offset = Integer.decode(stack.get(stack.size() - 1).getAsString());
        int size = Integer.decode(stack.get(stack.size() - 2).getAsString());

        String returnData = memory.substring(2 + offset * 2, 2 + offset * 2 + size * 2);
        return Integer.decode("0x"+returnData);
    }

    public static String convertIntegerToHex256Bit(int number) {
        BigInteger bigInt = BigInteger.valueOf(number);

        return String.format("%064x", bigInt);
    }

    public static String padHexStringTo256Bit(String hexString) {
        if (hexString.startsWith("0x")) {
            hexString = hexString.substring(2);
        }

        int length = hexString.length();
        int targetLength = 64;

        if (length >= targetLength) {
            return hexString.substring(0, targetLength);
        }

        return "0".repeat(targetLength - length) +
                hexString;
    }

}