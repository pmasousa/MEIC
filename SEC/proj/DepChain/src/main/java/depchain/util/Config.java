package depchain.util;

import java.util.HashMap;
import java.util.Map;

public class Config {
    // Static configuration for blockchain members (id, address, public key, etc.)
    public static final String LEADER_ID = "node1";
    
    // A simple map for id to IP:port (in a real system, keys would also be included)
    public static final Map<String, String> MEMBERS = new HashMap<>();
    
    static {
        // Example static membership
        MEMBERS.put("node1", "127.0.0.1:9001");
        MEMBERS.put("node2", "127.0.0.1:9002");
        MEMBERS.put("node3", "127.0.0.1:9003");
    }
}
