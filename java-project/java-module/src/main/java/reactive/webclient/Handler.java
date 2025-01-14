package reactive.webclient;

import org.springframework.stereotype.Service;
import org.springframework.web.reactive.function.server.ServerRequest;
import org.springframework.web.reactive.function.server.ServerResponse;
import reactor.core.publisher.Mono;

@Service
public class Handler {

    public Mono<ServerResponse> hello(ServerRequest serverRequest) {
        Mono<String> body = Mono.just("Hello Flux!");
        return ServerResponse.ok().body(body, String.class);
    }
}
