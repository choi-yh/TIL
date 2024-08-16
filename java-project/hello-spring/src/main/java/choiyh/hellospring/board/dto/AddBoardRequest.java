package choiyh.hellospring.board.dto;

import choiyh.hellospring.board.Board;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;

@NoArgsConstructor
@AllArgsConstructor
@Getter
public class AddBoardRequest {

    private String title;

    private String content;

    private String author;

    public Board toEntity(String author) {
        return Board.builder()
                .title(title)
                .content(content)
                .author(author)
                .build();
    }
}