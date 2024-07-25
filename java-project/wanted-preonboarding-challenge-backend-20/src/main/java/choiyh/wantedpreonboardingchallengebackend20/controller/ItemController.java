package choiyh.wantedpreonboardingchallengebackend20.controller;

import choiyh.wantedpreonboardingchallengebackend20.domain.Item;
import choiyh.wantedpreonboardingchallengebackend20.service.ItemService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;

@Controller
public class ItemController {

    private final ItemService itemService;

    @Autowired
    public ItemController(ItemService itemService) {
        this.itemService = itemService;
    }

    @GetMapping("/items")
    @ResponseBody
    public List<Item> getAll() {
        // TODO: requestParam 으로 paging 처리 할 것.

        return itemService.getAll();
    }

    @GetMapping("/items/{id}")
    @ResponseBody
    public Item getItem(@PathVariable("id") Long id) {
        // TODO: NoSuchElementException("No value present") 예외 처리
        return itemService.getItem(id);
    }
}
