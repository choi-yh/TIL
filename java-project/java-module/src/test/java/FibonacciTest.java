import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class FibonacciTest {

    @Test
    void normal() {
        assertEquals(377, Fibonacci.normal(13));
    }

    @Test
    void dp() {
        assertEquals(377, Fibonacci.dp(13));
    }

    @Test
    void memoization() {
        assertEquals(377, Fibonacci.memoization(13));
    }
}