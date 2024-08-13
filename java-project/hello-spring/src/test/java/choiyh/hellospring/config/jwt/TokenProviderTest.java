package choiyh.hellospring.config.jwt;

import choiyh.hellospring.user.User;
import io.jsonwebtoken.Jwts;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.userdetails.UserDetails;

import java.time.Duration;
import java.util.Date;
import java.util.Map;

import static org.assertj.core.api.Assertions.assertThat;

@SpringBootTest
public class TokenProviderTest {

    @Autowired
    private TokenProvider tokenProvider;

    @Autowired
    private JwtProperties jwtProperties;

    @Test
    public void generateToken() {

        // given. 토큰 정보 추가를 위한 유저 생성
        User user = User.builder()
                .email("test@email.com")
                .password("password")
                .build();

        // when. 토큰 생성 generateToken() 사용
        String token = tokenProvider.generateToken(user, Duration.ofDays(14));

        // then. 올바르게 생성된 토큰인지 확인
        Long userId = Jwts.parser()
                .setSigningKey(jwtProperties.getSecretKey())
                .parseClaimsJws(token)
                .getBody()
                .get("id", Long.class);

        assertThat(userId).isEqualTo(user.getId());

    }

    @Test
    public void validateToken_valid() {

        // given. 정상 토큰 생성
        String token = JwtFactory.withDefaultValues()
                .createToken(jwtProperties);


        // when. validateToken() 호출
        boolean result = tokenProvider.validToken(token);

        // then. true
        assertThat(result).isTrue();

    }

    @Test
    public void validateToken_invalid() {

        // given. 만료된 토큰 생성
        Date expiry = new Date(new Date().getTime() - Duration.ofDays(7).toMillis());
        String invalidToken = JwtFactory.builder()
                .expiration(expiry)
                .build()
                .createToken(jwtProperties);

        // when. validateToken() 호출
        boolean result = tokenProvider.validToken(invalidToken);

        // then. false
        assertThat(result).isFalse();

    }

    @Test
    public void getAuthentication() {

        // given. 유저 설정 및 토큰 생성
        String email = "test@email.com";
        String token = JwtFactory.builder()
                .subject(email)
                .build()
                .createToken(jwtProperties);

        // when. 인증 객체 받기
        Authentication authentication = tokenProvider.getAuthentication(token);

        // then. 설정한 유저와 맞는지 확인
        assertThat(((UserDetails) authentication.getPrincipal()).getUsername()).isEqualTo(email);

    }

    @Test
    public void getUserId() {

        // given. 토큰 생성
        Long userId = 1L;
        String token = JwtFactory.builder()
                .claims(Map.of("id", userId))
                .build()
                .createToken(jwtProperties);

        // when
        Long id = tokenProvider.getUserId(token);

        // then
        assertThat(id).isEqualTo(userId);

    }
}
