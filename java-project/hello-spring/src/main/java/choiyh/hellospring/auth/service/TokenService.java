package choiyh.hellospring.auth.service;

import choiyh.hellospring.config.jwt.TokenProvider;
import choiyh.hellospring.user.User;
import choiyh.hellospring.user.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.time.Duration;

@RequiredArgsConstructor
@Service
public class TokenService {

    private final TokenProvider tokenProvider;
    private final RefreshTokenService refreshTokenService;
    private final UserService userService;

    public String createAccessToken(String refreshToken) {
        if (!tokenProvider.validToken(refreshToken)){
            throw new IllegalArgumentException("Unexpected refresh_token");
        }

        Long userId = refreshTokenService.findByRefreshToken(refreshToken)
                .getUserId();
        User user = userService.findById(userId);

        return tokenProvider.generateToken(user, Duration.ofDays(1));
    }

}
