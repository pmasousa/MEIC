package depchain.client;

import depchain.util.Config;
import depchain.network.UDPSender;

/**
 * A simple client library to submit requests to the blockchain.
 */
public class ClientLibrary {
    private UDPSender sender;
    
    public ClientLibrary() {
        sender = new UDPSender();
    }
    
    public void submitAppendRequest(String data) {
        try {
            // In this simplified example, we assume the leader is the coordinator.
            String leaderAddress = Config.MEMBERS.get(Config.LEADER_ID);
            String[] parts = leaderAddress.split(":");
            String host = parts[0];
            int port = Integer.parseInt(parts[1]);
            // In a real implementation, you might wrap the data in a protocol message.
            sender.send(host, port, data.getBytes());
            System.out.println("Submitted append request: " + data);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    public static void main(String[] args) {
        // Run the client to test submitting an append request.
        ClientLibrary client = new ClientLibrary();
        client.submitAppendRequest("Client request: Append this string.");
    }
}
