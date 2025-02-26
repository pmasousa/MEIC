package depchain.network;

import java.net.DatagramPacket;
import java.net.DatagramSocket;

public class UDPReceiver implements Runnable {
    private final int port;
    private volatile boolean running = true;
    
    public UDPReceiver(int port) {
        this.port = port;
    }
    
    public void stop() {
        running = false;
    }
    
    @Override
    public void run() {
        try (DatagramSocket socket = new DatagramSocket(port)) {
            while (running) {
                byte[] buffer = new byte[4096];
                DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
                socket.receive(packet);
                // Process packet (pass to appropriate layer)
                System.out.println("Received packet from " + packet.getAddress() + ":" + packet.getPort());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
