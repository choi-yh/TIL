package choiyh.hellospring.board.dto;

import choiyh.hellospring.board.Board;
import lombok.Getter;

@Getter
public class BoardListViewResponse {

    private final Long id;
    private final String title;
    private final String content;

    public BoardListViewResponse(Board board) {
        this.id = board.getId();
        this.title = board.getTitle();
        this.content = board.getContent();
    }

}
