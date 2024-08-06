package choiyh.hellospring.sample;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

public class JUnitTest {

    @DisplayName("1 + 2는 3이다") // 테스트명
    @Test // 테스트를 수행하기 위한 애너테이션
    public void junitTest() {
        int a = 1;
        int b = 2;

        int sum = 3;

        Assertions.assertEquals(sum, a + b);
    }

    @DisplayName("1 + 3는 4이다")
    @Test
    public void junitFailedTest() {
        int a = 1;
        int b = 3;

        int sum = 3;

        Assertions.assertNotEquals(sum, a + b);
    }

}
