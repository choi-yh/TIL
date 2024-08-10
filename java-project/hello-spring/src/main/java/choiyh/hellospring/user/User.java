package choiyh.hellospring.user;

import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.annotation.LastModifiedDate;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import java.time.LocalDateTime;
import java.util.Collection;
import java.util.List;

@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Getter
@Entity
public class User implements UserDetails { // spring security 에 있는 UserDetails 를 상속받아 인증 객체로 이용

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id", updatable = false)
    private Long id;

    @Column(name = "email", nullable = false, unique = true)
    private String email;

    @Column(name = "password", nullable = false)
    private String password;

    @Column(name = "created_at")
    @CreatedDate
    private LocalDateTime createdAt;

    @Column(name = "updated_at")
    @LastModifiedDate
    private LocalDateTime updatedAt;

    @Builder
    public User(String email, String password, String auth) {
        this.email = email;
        this.password = password;
    }

    // 나의 User 클래스가 spring security 의 UserDetail 객체를 상속(implements) 받아 내 애플리케이션의 인증 객체로 사용하기 때문에
    // getAuthorities() 를 구현해야 한다.
    // extends 상속은 그대로 사용 가능. implements 는 @Override 로 구현해야 한다.
    @Override // 권한 반환
    public Collection<? extends GrantedAuthority> getAuthorities() {
        return List.of(new SimpleGrantedAuthority("user")); // 사용자 이외의 권한이 필요해진다면 추가할 것.
    }

    // 이름과 패스워드라 고윳값으로 찾아오는 듯 함.
    @Override
    public String getUsername() {
        return email;
    }

    @Override
    public String getPassword() {
        return password;
    }

    @Override
    public boolean isAccountNonExpired() {
        // TODO: 계정 만료 확인 로직
        return true;
    }

    @Override
    public boolean isAccountNonLocked() {
        // TODO: 계정 잠금 확인 로직
        return true;
    }

    @Override
    public boolean isCredentialsNonExpired() {
        // TODO: 패스워드 만료 확인 로직
        return true;
    }

    @Override
    public boolean isEnabled() {
        // TODO: 계정 사용 가능 여부 확인 로직
        return true;
    }

}
