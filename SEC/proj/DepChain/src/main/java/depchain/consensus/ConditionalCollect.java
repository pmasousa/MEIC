package depchain.consensus;

import java.util.HashSet;
import java.util.Set;

/**
 * A simple implementation of a conditional collector that gathers messages until a certain condition is met.
 */
public class ConditionalCollect<T> {
    private final Set<T> collected = new HashSet<>();
    private final int threshold;
    
    public ConditionalCollect(int threshold) {
        this.threshold = threshold;
    }
    
    public synchronized void add(T message) {
        collected.add(message);
        notifyAll();
    }
    
    public synchronized Set<T> waitForCondition() throws InterruptedException {
        while (collected.size() < threshold) {
            wait();
        }
        return new HashSet<>(collected);
    }
}
