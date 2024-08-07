package choiyh.hellospring.member;

import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

// 기본 생성자. 엔티티는 반드시 기본 생성자가 존재해야 한다.
// 접근 제어자는 public 혹은 protected
// 파라미터가 없는 디폴트 생성자를 의미한다.
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@AllArgsConstructor // 모든 필드 값을 파라미터로 받는 생성자를 생성. 클래스의 모든 필드를 한 번에 초기화 가능
@Getter
@Entity // 데이터베이스의 테이블과 매핑되는 객체
public class Member {

    @Id // id 필드를 기본키로 지정
    @GeneratedValue(strategy = GenerationType.IDENTITY) // 기본키 자동 증가
    @Column(name = "id", updatable = false)
    private long id;

    @Column(name = "name", nullable = false)
    private String name;

    public void changeName(String name) {
        this.name = name;
    }
}
