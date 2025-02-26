package depchain.consensus;

import depchain.network.UDPSender;
import depchain.util.Config;

public class PerfectLinks {
    private UDPSender sender;
    
    public PerfectLinks() {
        this.sender = new UDPSender();
    }
    
    /**
     * Sends a message to a specified member with authentication.
     * Here, you would also attach a digital signature using CryptoUtils.
     */
    public void send(String memberId, byte[] message) {
        try {
            // Extract host and port from Config
            String address = Config.MEMBERS.get(memberId);
            String[] parts = address.split(":");
            String host = parts[0];
            int port = Integer.parseInt(parts[1]);
            
            // Optionally: sign the message before sending
            
            sender.send(host, port, message);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    /**
     * This method would be called by the network layer when a message is received.
     * It should verify the authenticity and deliver it to the consensus layer.
     */
    public void deliver(byte[] message) {
        // Verify signature and process message
    }
}
