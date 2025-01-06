package reactive;

import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

import java.util.List;

public class Sample {
    public static void main(String[] args) {
        // https://adjh54.tistory.com/232
        // mono example
        Mono.just("hello, world!")
                .map(String::toUpperCase)
                .flatMap(s -> Mono.just("Mono: " + s))
                .subscribe(System.out::println);

        // flux example
        Flux.just("apple", "banana", "cherry")
                .map(String::toUpperCase)
                .flatMap(s -> Flux.just("Flux: " + s))
                .subscribe(System.out::println);

        // flux to list
        List<String> fruits = Flux.just("apple", "banana", "cherry")
                .map(String::toUpperCase)
                .flatMap(s -> Flux.just("Flux: " + s))
                .collectList()
                .block();
        System.out.println(fruits);
    }
}
