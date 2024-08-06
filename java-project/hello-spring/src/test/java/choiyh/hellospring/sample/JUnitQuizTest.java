package choiyh.hellospring.sample;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;


public class JUnitQuizTest {

    @Test
    public void junitTest() {
        String name1 = "홍길동";
        String name2 = "홍길동";
        String name3 = "홍길은";

        // 1. 모든 변수가 null 이 아닌지 확인
        assertThat(name1).isNotNull();
        assertThat(name2).isNotNull();
        assertThat(name3).isNotNull();

        // 2. name1 과 name2 가 같은지 확인
        assertThat(name1).isEqualTo(name2);

        // 3. name1 과 name3 이 다른지 확인
        assertThat(name1).isNotEqualTo(name3);

    }

    @Test
    public void junitTest2() {
        int num1 = 15;
        int num2 = 0;
        int num3 = -5;

        // 1. num1 은 양수인지 확인
        assertThat(num1).isPositive();

        // 2. num2 은 0 인지 확인
        assertThat(num2).isZero();

        // 3. num3 은 음수인지 확인
        assertThat(num3).isNegative();

        // 4. num1 은 num2 보다 큰지 확인
        assertThat(num1).isGreaterThan(num2);

        // 5. num3 은 num2 보다 작은지 확인
        assertThat(num3).isLessThan(num2);

    }

}
