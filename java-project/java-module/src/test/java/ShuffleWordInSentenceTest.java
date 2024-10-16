import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class ShuffleWordInSentenceTest {

    @Test
    public void shuffle() {
        assertEquals("expected? is what and actual is what", ShuffleWordInSentence.shuffle("what is actual and what is expected?"));
    }

}
