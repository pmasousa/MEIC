package depchain.blockchain;

import java.util.List;
import java.util.ArrayList;
import depchain.util.Config;
import depchain.network.UDPReceiver;
import depchain.consensus.ByzantineConsensus;

/**
 * Represents a blockchain node that maintains the blockchain (an in-memory list of strings).
 */
public class BlockchainMember {
    private List<String> blockchain;
    private ByzantineConsensus consensus;
    
    public BlockchainMember() {
        blockchain = new ArrayList<>();
        consensus = new ByzantineConsensus();
    }
    
    public void startReceiver(int port) {
        UDPReceiver receiver = new UDPReceiver(port);
        Thread receiverThread = new Thread(receiver);
        receiverThread.start();
    }
    
    public void appendString(String data) {
        consensus.propose(data);
        blockchain.add(data);
        System.out.println("Appended data: " + data);
    }
    
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Usage: java BlockchainMember <nodeId>");
            return;
        }
        String nodeId = args[0];
        // Determine the port from configuration using nodeId
        String address = Config.MEMBERS.get(nodeId);
        String[] parts = address.split(":");
        int port = Integer.parseInt(parts[1]);
        
        BlockchainMember member = new BlockchainMember();
        member.startReceiver(port);
        
        // For demo purposes, simulate appending a string.
        member.appendString("Hello, DepChain from " + nodeId + "!");
    }
}
