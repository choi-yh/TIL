package choiyh.wantedpreonboardingchallengebackend20.service;

import choiyh.wantedpreonboardingchallengebackend20.domain.User;
import choiyh.wantedpreonboardingchallengebackend20.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class UserService {

    UserRepository userRepository;

    @Autowired
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public boolean validateUser(Long id) {
        return userRepository.findById(id).isPresent();
    }

}
