package choiyh.wantedpreonboardingchallengebackend20.repository;

import choiyh.wantedpreonboardingchallengebackend20.domain.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {
}
