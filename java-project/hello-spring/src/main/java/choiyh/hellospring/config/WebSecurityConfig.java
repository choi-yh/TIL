//package choiyh.hellospring.config;
//
//import choiyh.hellospring.user.service.UserDetailService;
//import lombok.RequiredArgsConstructor;
//import org.springframework.context.annotation.Bean;
//import org.springframework.context.annotation.Configuration;
//import org.springframework.security.authentication.AuthenticationManager;
//import org.springframework.security.authentication.ProviderManager;
//import org.springframework.security.authentication.dao.DaoAuthenticationProvider;
//import org.springframework.security.config.annotation.web.builders.HttpSecurity;
//import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
//import org.springframework.security.config.annotation.web.configuration.WebSecurityCustomizer;
//import org.springframework.security.config.annotation.web.configurers.AbstractHttpConfigurer;
//import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
//import org.springframework.security.web.SecurityFilterChain;
//import org.springframework.security.web.util.matcher.AntPathRequestMatcher;
//
//@Configuration
//@EnableWebSecurity
//@RequiredArgsConstructor
//public class WebSecurityConfig {
//
//    private final UserDetailService userDetailService;
//
//    // spring security 기능 비활성화
//    // 인증, 인가를 모든 곳에 적용하지는 않는다. (일반적으로 정적 리소스에 설정)
//    @Bean
//    public WebSecurityCustomizer configure() {
//        return (web) -> web.ignoring()
////                .requestMatchers(toH2Console())
//                .requestMatchers(new AntPathRequestMatcher("/static/**"));
//    }
//
//    // 특정 HTTP 요청에 대한 웹 기반 보안 구성
//    // 인증/인가, 로그인, 로그아웃 관련 설정 가능
//    @Bean
//    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
//        return http
//                .authorizeHttpRequests(auth -> auth // 인증, 인가 설정
//                        .requestMatchers( // 특정 요청과 일치하는 url 에 대한 액세스 설정
//                                new AntPathRequestMatcher("/login"),
//                                new AntPathRequestMatcher("/signup"),
//                                new AntPathRequestMatcher("/user")
//                        ).permitAll() // 해당 url 은 누구나 접근 가능
//                        .anyRequest() // 위에 설정한 url 을 제외한 요청에 대한 설정
//                        .authenticated() // 인가는 없지만 인증된 상태여야 접근 가능
//                )
//                .formLogin(formLogin -> formLogin //  폼 기반 로그인 설정
//                        .loginPage("/login")
//                        .defaultSuccessUrl("/boards")
//                )
//                .logout(logout -> logout
//                        .logoutSuccessUrl("/login")
//                        .invalidateHttpSession(true) // 로그아웃 이후 세션 전체 삭제 여부 설정
//                )
//                .csrf(AbstractHttpConfigurer::disable)
//                .build();
//    }
//
//    // 인증 관리자 관련 설정
//    // 사용자 정보를 가져올 서비스 재정이, 인증 방법 (LDAP, JDBC 기반 인증 등) 설정할 때 사용
//    @Bean
//    public AuthenticationManager authenticationManager(HttpSecurity http
//            , BCryptPasswordEncoder bCryptPasswordEncoder
//    ) throws Exception {
//        DaoAuthenticationProvider authProvider = new DaoAuthenticationProvider();
//        authProvider.setUserDetailsService(userDetailService);
//        authProvider.setPasswordEncoder(bCryptPasswordEncoder);
//        return new ProviderManager(authProvider);
//    }
//
//    // 패스워드 인코더로 사용할 빈 등록
//    @Bean
//    public BCryptPasswordEncoder bCryptPasswordEncoder() {
//        return new BCryptPasswordEncoder();
//    }
//
//}
