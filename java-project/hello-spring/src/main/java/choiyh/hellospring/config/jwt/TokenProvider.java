package choiyh.hellospring.config.jwt;

import choiyh.hellospring.user.User;
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Header;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import lombok.RequiredArgsConstructor;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.stereotype.Service;

import java.time.Duration;
import java.util.Collections;
import java.util.Date;
import java.util.Set;

@RequiredArgsConstructor
@Service
public class TokenProvider {

    private final JwtProperties jwtProperties;

    public String generateToken(User user, Duration expiredAt) {
        Date now = new Date();
        Date expiry = new Date(now.getTime() + expiredAt.toMillis());
        return makeToken(expiry, user);
    }

    private String makeToken(Date expiry, User user) {
        Date now = new Date();

        return Jwts.builder()
                .setHeaderParam(Header.TYPE, Header.JWT_TYPE) // 헤더 typ (type): JWT
                .setIssuer(jwtProperties.getIssuer()) // 내용 iss (issuer): 토큰 발급자 (choi-yh) properties 에서 설정 한 값
                .setIssuedAt(now) // 내용 iat (issued_at): 토큰 발급 시간 (현재 시간)
                .setExpiration(expiry) // 내용 exp (expiration): 토큰 만료 시간 (NumericDate 형식). 현재 시간 이후로 설정
                .setSubject(user.getEmail()) // 내용 sub (subject): 토큰 제목 (유저 이메일)
//                .setAudience() // 내용 aud: 토큰 대상자 (audience)
//                .setNotBefore() // 내용 nbf: 토큰 활성 날짜. 해당 값이 지나야 토큰이 처리 됨. (NumericDate 형식)
                .claim("id", user.getId()) // 클레임 id: 유저 ID
                // 서명: 비밀 값과 함께 해시 값을 HS256 방식으로 암호화
                .signWith(SignatureAlgorithm.HS256, jwtProperties.getSecretKey())
                .compact();
    }

    public boolean validToken(String token) {
        try {
            Jwts.parser()
                    .setSigningKey(jwtProperties.getSecretKey()) // 비밀 값으로 복호화
                    .parseClaimsJws(token);

            return true;
        } catch (Exception e) { // 복호화 과정에서 에러 발생시 유효하지 않은 토큰
            return false;
        }
    }

    public Authentication getAuthentication(String token) {
        Claims claims = getClaims(token); // 여기에는 exception handling 없어도 되나?
        Set<SimpleGrantedAuthority> authorities = Collections.singleton(new SimpleGrantedAuthority("ROLE_USER"));

        // 여기서는 spring security 의 userdetails 가 필요함
        return new UsernamePasswordAuthenticationToken(
                new org.springframework.security.core.userdetails.User(claims.getSubject(), "", authorities),
                token, authorities
        );
    }

    public Long getUserId(String token) {
        Claims claims = getClaims(token);
        return claims.get("id", Long.class);
    }

    private Claims getClaims(String token) {
        return Jwts.parser()
                .setSigningKey(jwtProperties.getSecretKey())
                .parseClaimsJws(token)
                .getBody();
    }

}
