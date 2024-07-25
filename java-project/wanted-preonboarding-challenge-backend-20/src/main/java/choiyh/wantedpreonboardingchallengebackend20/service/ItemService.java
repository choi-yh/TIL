package choiyh.wantedpreonboardingchallengebackend20.service;

import choiyh.wantedpreonboardingchallengebackend20.domain.Item;
import choiyh.wantedpreonboardingchallengebackend20.repository.ItemRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
public class ItemService {

    private final ItemRepository itemRepository;

    @Autowired
    public ItemService(ItemRepository jpaItemRepository) {
        this.itemRepository = jpaItemRepository;
    }

    public List<Item> getAll() {
        return itemRepository.findAll();
    }

    public Item getItem(Long id) {
        Optional<Item> item = itemRepository.findById(id);
        return item.orElseThrow();
    }
}
