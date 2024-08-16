package choiyh.hellospring.auth.controller;

import choiyh.hellospring.auth.dto.CreateAccessTokenRequest;
import choiyh.hellospring.auth.dto.CreateAccessTokenResponse;
import choiyh.hellospring.auth.service.TokenService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;

@RequiredArgsConstructor
@Controller
@RequestMapping("/api/v1")
public class TokenApiController {

    private final TokenService tokenService;

    @PostMapping("/token")
    public ResponseEntity<CreateAccessTokenResponse> createAccessToken(@RequestBody CreateAccessTokenRequest request) {
        String accessToken = tokenService.createAccessToken(request.getRefreshToken());

        return ResponseEntity.status(HttpStatus.CREATED)
                .body(new CreateAccessTokenResponse(accessToken));
    }

}
