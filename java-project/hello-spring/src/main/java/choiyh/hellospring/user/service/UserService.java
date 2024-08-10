package choiyh.hellospring.user.service;

import choiyh.hellospring.user.User;
import choiyh.hellospring.user.UserRepository;
import choiyh.hellospring.user.dto.AddUserRequest;
import lombok.RequiredArgsConstructor;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

@RequiredArgsConstructor
@Service
public class UserService {

    private final UserRepository userRepository;
    private final BCryptPasswordEncoder bCryptPasswordEncoder;

    public Long save(AddUserRequest dto) {
        return userRepository.save(User.builder()
                        .email(dto.getEmail())
                        // 패스워드 인코딩용으로 등록한 빈을 사용해서 암호화
                        .password(bCryptPasswordEncoder.encode(dto.getPassword()))
                        .build()
                )
                .getId();
    }

}
