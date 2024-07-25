package choiyh.wantedpreonboardingchallengebackend20.repository;

import choiyh.wantedpreonboardingchallengebackend20.domain.Item;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;


@Repository
public interface ItemRepository extends JpaRepository<Item, Long> {

}
