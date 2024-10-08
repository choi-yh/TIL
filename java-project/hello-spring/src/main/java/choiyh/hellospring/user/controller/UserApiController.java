package choiyh.hellospring.user.controller;

import choiyh.hellospring.user.service.UserService;
import choiyh.hellospring.user.dto.AddUserRequest;
import choiyh.hellospring.user.dto.LoginUserRequest;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.web.authentication.logout.SecurityContextLogoutHandler;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@RequiredArgsConstructor
@Controller
@RequestMapping("/api/v1")
public class UserApiController {

    private final UserService userService;

    @PostMapping("/signup")
    public String signup(AddUserRequest request) {
        userService.save(request);
        return "redirect:/login";
    }

    @PostMapping("/login")
    public String login(LoginUserRequest request) {
        return "redirect:/login";
    }

    @PostMapping("/logout")
    public String logout(HttpServletRequest request, HttpServletResponse response) {
        new SecurityContextLogoutHandler().logout(request, response, SecurityContextHolder.getContext().getAuthentication());
        return "redirect:/login";
    }

}
