package choiyh.hellospring.sample;

import org.aspectj.lang.annotation.After;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class JUnitCycleQuizTest {

    // 1. 각각의 테스트 시작 전에 "Hello!" 를 출력하는 메서드
    @BeforeEach
    public void beforeEach() {
        System.out.println("Hello!");
    }

    // 2. 모든 테스트를 마치고 "Bye!" 를 출력하는 메서드
    @AfterAll
    public static void afterAll() {
        System.out.println("Bye!");
    }

    @Test
    public void junitQuiz3() {
        System.out.println("This is first test");
    }

    @Test
    public void junitQuiz4() {
        System.out.println("This is second test");
    }

}
