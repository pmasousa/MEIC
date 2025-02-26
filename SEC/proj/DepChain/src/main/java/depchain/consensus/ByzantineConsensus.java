package depchain.consensus;

import depchain.util.Config;
import java.util.logging.Logger;

/**
 * A simplified implementation of the Byzantine Read/Write Epoch Consensus algorithm.
 * For this stage, we assume a static membership and a correct leader.
 */
public class ByzantineConsensus {
    private static final Logger logger = Logger.getLogger(ByzantineConsensus.class.getName());
    private PerfectLinks perfectLinks;
    private ConditionalCollect<String> conditionalCollect;
    
    public ByzantineConsensus() {
        this.perfectLinks = new PerfectLinks();
        // Threshold can be set as needed (for example, N - f)
        this.conditionalCollect = new ConditionalCollect<>(Config.MEMBERS.size());
    }
    
    /**
     * This method initiates the consensus on a proposed value.
     */
    public void propose(String value) {
        // Leader sends the proposal to all members
        for (String memberId : Config.MEMBERS.keySet()) {
            perfectLinks.send(memberId, value.getBytes());
        }
        // Wait for responses (this is highly simplified)
        try {
            conditionalCollect.waitForCondition();
            decide(value);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
    
    /**
     * Called when consensus is reached.
     */
    public void decide(String value) {
        logger.info("Consensus reached: " + value);
        // Upcall to the blockchain layer
    }
    
    // This method would be called upon receipt of a message from PerfectLinks.
    public void onReceive(String message) {
        conditionalCollect.add(message);
    }
}
