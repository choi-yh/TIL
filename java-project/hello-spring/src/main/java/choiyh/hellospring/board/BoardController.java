package choiyh.hellospring.board;

import choiyh.hellospring.board.dto.AddBoardRequest;
import choiyh.hellospring.board.dto.BoardResponse;
import choiyh.hellospring.board.dto.UpdateBoardRequest;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RequiredArgsConstructor
@RestController
public class BoardController {

    @Autowired
    private final BoardService boardService;

    @PostMapping("/board")
    public ResponseEntity<Board> addBoard(@RequestBody AddBoardRequest request) {
        Board board = boardService.save(request);
        return ResponseEntity.status(HttpStatus.CREATED)
                .body(board);
    }

    @GetMapping("/boards")
    public ResponseEntity<List<BoardResponse>> findAll() {
        List<BoardResponse> boards = boardService.findAll()
                .stream()
                .map(BoardResponse::new)
                .toList();

        return ResponseEntity.status(HttpStatus.OK)
                .body(boards);
    }

    @GetMapping("/board/{id}")
    public ResponseEntity<BoardResponse> getBoard(@PathVariable Long id) {
        // TODO: 없는 id 에 대한 exception handling
        Board board = boardService.findById(id);
        return ResponseEntity.status(HttpStatus.OK)
                .body(new BoardResponse(board));
    }

    @PutMapping("/board/{id}")
    public ResponseEntity<BoardResponse> updateBoard(
            @PathVariable Long id,
            @RequestBody UpdateBoardRequest request) {

        // TODO: 없는 id 에 대한 exception handling
        Board updateBoard = boardService.update(id, request);

        return ResponseEntity.ok()
                .body(new BoardResponse(updateBoard));
    }

    @DeleteMapping("/board/{id}")
    public ResponseEntity<Void> deleteBoard(@PathVariable Long id) {
        // TODO: 없는 id 에 대한 exception handling
        boardService.delete(id);

        return ResponseEntity.ok()
                .build();
    }

}
