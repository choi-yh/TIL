package choiyh.hellospring.member;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController // router 역할을 하는 애너테이션
public class MemberController {

    @Autowired
    MemberService memberService;

    @GetMapping("/members")
    public List<Member> getAllMembers() {
        List<Member> members = memberService.getAllMembers();
        return members;
    }
}
