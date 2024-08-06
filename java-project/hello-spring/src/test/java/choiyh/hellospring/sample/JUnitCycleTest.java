package choiyh.hellospring.sample;

import org.junit.jupiter.api.*;

public class JUnitCycleTest {
    // 전체 테스트를 시작하기 전에 1회 실행하므로 메서드는 static 으로 선언
    // ex) 데이터베이스 연결, 테스트 환경 초기화하는 경우
    @BeforeAll
    static void beforeAll() {
        System.out.println("@BeforeAll");
    }

    // 테스트 케이스를 시작하기 전마다 실행
    // ex) 테스트 메서드에서 사용하는 객체를 초기화하거나 테스트에 필요한 값을 채워넣을 때.
    @BeforeEach
    public void beforeEach() {
        System.out.println("@BeforeEach");
    }

    @Test
    public void test1() {
        System.out.println("test1");
    }

    @Test
    public void test2() {
        System.out.println("test2");
    }

    @Test
    public void test3() {
        System.out.println("test3");
    }

    // 전체 테스트를 마치고 종료하기 전에 1회 실행하므로 메서드는 static 으로 선언
    // ex) DB 커넥션 종료, 공통 자원 해제 등
    @AfterAll
    static void afterAll() {
        System.out.println("@AfterAll");
    }


    @AfterEach // 전체 테스트를 마치고 종료하기 전에 1회 실행하므로 메서드는 static 으로 선언
    public void afterEach() {
        System.out.println("@AfterEach");
    }

}
