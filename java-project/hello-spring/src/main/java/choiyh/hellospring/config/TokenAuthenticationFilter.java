package choiyh.hellospring.config;

import choiyh.hellospring.config.jwt.TokenProvider;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;

/*
    필터는 요청을 처리하기 위한 로직으로 전달되기 전후에 URL 패턴에 맞는 모든 요청을 처리하는 기능 제공.
    Interceptor 같은 개념이라고 이해하면 되려나?
    (해당 클래스는 토큰 인증에 대한 요청 처리를 위한 필터)

    요청이 오면 헤더 값을 비교 -> 토큰 탐색 -> 유효 토큰인 경유 security context holder 에 인증 정보 저장

    security context.
        인증 객체가 저장되는 보관소.
        스레드 로컬(스레드마다 공간 할당)에 저장됨. -> 아무 곳에서나 참조 가능하고, 다른 스레드와 공유하지 않기 때문에 독립적인 사용 가능
        security context 객체를 저장하는 객체가 security context holder
 */
@RequiredArgsConstructor
public class TokenAuthenticationFilter extends OncePerRequestFilter {

    private final TokenProvider tokenProvider;
    private final static String HEADER_AUTHORIZATION = "Authorization";
    private final static String TOKEN_PREFIX = "Bearer ";

    @Override
    protected void doFilterInternal(
            HttpServletRequest request,
            HttpServletResponse response,
            FilterChain filterChain
    ) throws ServletException, IOException {

        String authorizationHeader = request.getHeader(HEADER_AUTHORIZATION);
        String token = getAccessToken(authorizationHeader);

        if (tokenProvider.validToken(token)) {
            Authentication authentication = tokenProvider.getAuthentication(token);
            SecurityContextHolder.getContext().setAuthentication(authentication);
        }

        filterChain.doFilter(request, response);
    }

    private String getAccessToken(String authorizationHeader) {
        if (authorizationHeader != null && authorizationHeader.startsWith(TOKEN_PREFIX)) {
            return authorizationHeader.substring(TOKEN_PREFIX.length());
        }

        return null;
    }

}
