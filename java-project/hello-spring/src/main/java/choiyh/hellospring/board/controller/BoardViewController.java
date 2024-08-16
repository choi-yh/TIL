package choiyh.hellospring.board.controller;

import choiyh.hellospring.board.Board;
import choiyh.hellospring.board.service.BoardService;
import choiyh.hellospring.board.dto.BoardListViewResponse;
import choiyh.hellospring.board.dto.BoardViewResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.List;

@RequiredArgsConstructor
@Controller
public class BoardViewController {

    private final BoardService boardService;

    @GetMapping("/boards")
    public String getBoards(Model model) {
        List<BoardListViewResponse> boards = boardService.findAll().stream()
                .map(BoardListViewResponse::new)
                .toList();
        model.addAttribute("boards", boards);

        return "board/boardList";
    }

    @GetMapping("/boards/{id}")
    public String getBoards(@PathVariable Long id, Model model) {
        Board board = boardService.findById(id);
        model.addAttribute("board", new BoardViewResponse(board));

        return "board/board";
    }

    @GetMapping("/new-board")
    public String newBoard(@RequestParam(required = false) Long id, Model model) {
        // 생성하는 케이스
        if (id == null) {
            model.addAttribute("board", new BoardViewResponse());
        } else {
            Board board = boardService.findById(id);
            model.addAttribute("board", new BoardViewResponse(board));
        }

        return "board/newBoard";
    }

}
