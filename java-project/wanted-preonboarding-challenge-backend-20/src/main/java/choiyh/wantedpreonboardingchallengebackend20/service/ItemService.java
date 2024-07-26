package choiyh.wantedpreonboardingchallengebackend20.service;

import choiyh.wantedpreonboardingchallengebackend20.domain.Item;
import choiyh.wantedpreonboardingchallengebackend20.repository.ItemRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class ItemService {

    private final ItemRepository itemRepository;

    @Autowired
    public ItemService(ItemRepository itemRepository) {
        this.itemRepository = itemRepository;
    }

    public List<Item> getAll() {
        return itemRepository.findAll();
    }

    public Item getItem(Long id) {
        Optional<Item> item = itemRepository.findById(id);
        return item.orElseThrow();
    }

    public Item save(Item item) {
        return itemRepository.save(item);
    }

    public Item buy(Long id, Long userID) {
        Optional<Item> item = itemRepository.findById(id);

        Item updateItem = item.orElseThrow();

        if (!updateItem.getStatus().equals(Item.Status.Sale)) {
            // TODO: 판매 완료 및 거래 중 예외 처리
        }

        updateItem.setStatus(Item.Status.Reserved);
        updateItem.getSeller().setId(userID);

        return itemRepository.save(updateItem);
    }

}
