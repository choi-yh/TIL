package choiyh.wantedpreonboardingchallengebackend20.controller;

import choiyh.wantedpreonboardingchallengebackend20.domain.Item;
import choiyh.wantedpreonboardingchallengebackend20.domain.User;
import choiyh.wantedpreonboardingchallengebackend20.service.ItemService;
import choiyh.wantedpreonboardingchallengebackend20.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
public class ItemController {

    private final ItemService itemService;
    private final UserService userService;

    @Autowired
    public ItemController(ItemService itemService, UserService userService) {
        this.itemService = itemService;
        this.userService = userService;
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

    @PostMapping("/item/register")
    @ResponseBody
    public Item registerItem(@RequestBody Item item) {
        if (!userService.validateUser(item.getSeller().getId())) {
            // TODO: invalid user 에러 발생
        }

        return itemService.save(item);
    }

    @PostMapping("item/{id}/buy")
    @ResponseBody
    public Item buy(@PathVariable Long id,
                    @RequestBody Long userID) {

        if (!userService.validateUser(userID)) {
            // TODO: invalid user 에러 처리
        }

        // TODO: NoSuchElementException 예외 처리
        return itemService.buy(id, userID);
    }

}
