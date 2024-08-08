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

    public Board toEntity() {
        return Board.builder()
                .title(title)
                .content(content)
                .build();
    }
}