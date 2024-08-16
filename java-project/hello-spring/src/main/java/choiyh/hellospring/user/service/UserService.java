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

    public Long save(AddUserRequest dto) {
        BCryptPasswordEncoder encoder = new BCryptPasswordEncoder(); // DI cycle 발생으로 인한 새 객체 생성

        return userRepository.save(User.builder()
                        .email(dto.getEmail())
                        // 패스워드 인코딩용으로 등록한 빈을 사용해서 암호화
                        .password(encoder.encode(dto.getPassword()))
                        .build()
                )
                .getId();
    }

    public User findById(Long userId) {
        return userRepository.findById(userId)
                .orElseThrow(() -> new IllegalArgumentException("Unexpected user_id"));
    }

    public User findByEmail(String email) {
        return userRepository.findByEmail(email)
                .orElseThrow(() -> new IllegalArgumentException("Unexpected user_id"));
    }

}
