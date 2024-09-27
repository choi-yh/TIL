package com.example.jump2springboot.gamerecord;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Controller
public class User {
    private final String DATA_DIR = "/Users/younghyo/Projects/jump2springboot/data";
    private final ObjectMapper objectMapper = new ObjectMapper();

    @GetMapping("/api/gamerecord/users")
    public ResponseEntity<?> getUsers() {
        try {
            List<Map<String, Object>> users = objectMapper.readValue(
                    Files.readAllBytes(Paths.get(DATA_DIR, "records.json")),
                    new TypeReference<>() {
                    }
            );

            List<Map<String, String>> resp = users.stream().
                    map(user -> {
                        Map<String, String> info = new HashMap<>();
                        info.put("username", user.get("username").toString());
                        info.put("tag", user.get("tag").toString());
                        return info;
                    }).
                    sorted(
                            Comparator.comparing((Map<String, String> user) -> user.get("username")).thenComparing(user -> user.get("tag"))
                    ).
                    toList()
            ;

            return ResponseEntity.ok(resp);
        } catch (IOException e) {
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
        }
    }

    @GetMapping("/api/gamerecord/winrate")
    // 여기에 코드를 작성하세요.
    public ResponseEntity<?> getWinrate(@RequestParam String username, String tag) {
        try {
            if (username.isEmpty() || tag.isEmpty()) {
                return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("invalid parameter");
            }

            List<Map<String, Object>> users = objectMapper.readValue(
                    Files.readAllBytes(Paths.get(DATA_DIR, "records.json")),
                    new TypeReference<>() {
                    });

            for (Map<String, Object> user : users) {
                if (user.get("username").equals(username) && user.get("tag").equals(tag)) {
                    Map<String, Integer> response = new HashMap<>();

                    int win = (int) user.get("win");
                    int lose = (int) user.get("lose");

                    int winrate = (int) (win / (double) (win+lose) * 100) ;
                    response.put("winrate", winrate);

                    return ResponseEntity.ok(response);
                }
            }

            return ResponseEntity.status(HttpStatus.NOT_FOUND).body("data not found");
        } catch (IOException e) {
            e.printStackTrace();
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
        }
    }
}
