package choiyh.hellospring.board.dto;

import choiyh.hellospring.board.Board;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@NoArgsConstructor
@Getter
public class BoardViewResponse {

    private Long id;
    private String title;
    private String content;
    private String author;
    private LocalDateTime createdAt;

    public BoardViewResponse(Board board) {
        this.id = board.getId();
        this.title = board.getTitle();
        this.content = board.getContent();
        this.createdAt = board.getCreatedAt();
        this.author = board.getAuthor();
    }

}
