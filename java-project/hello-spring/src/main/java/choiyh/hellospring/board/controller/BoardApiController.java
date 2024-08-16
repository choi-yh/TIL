package choiyh.hellospring.board.controller;

import choiyh.hellospring.board.Board;
import choiyh.hellospring.board.service.BoardService;
import choiyh.hellospring.board.dto.AddBoardRequest;
import choiyh.hellospring.board.dto.BoardResponse;
import choiyh.hellospring.board.dto.UpdateBoardRequest;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.security.Principal;

@RequiredArgsConstructor
@RestController
public class BoardApiController {

    @Autowired
    private final BoardService boardService;

    @PostMapping("/boards")
    public ResponseEntity<Board> addBoard(@RequestBody AddBoardRequest request, Principal principal) {
        Board board = boardService.save(request, principal.getName());
        return ResponseEntity.status(HttpStatus.CREATED)
                .body(board);
    }

    // view test 를 위한 주석처리
//    @GetMapping("/boards")
//    public ResponseEntity<List<BoardResponse>> findAll() {
//        List<BoardResponse> boards = boardService.findAll()
//                .stream()
//                .map(BoardResponse::new)
//                .toList();
//
//        return ResponseEntity.status(HttpStatus.OK)
//                .body(boards);
//    }

//    @GetMapping("/boards/{id}")
//    public ResponseEntity<BoardResponse> getBoard(@PathVariable Long id) {
//        // TODO: 없는 id 에 대한 exception handling
//        Board board = boardService.findById(id);
//        return ResponseEntity.status(HttpStatus.OK)
//                .body(new BoardResponse(board));
//    }

    @PutMapping("/boards/{id}")
    public ResponseEntity<BoardResponse> updateBoard(
            @PathVariable Long id,
            @RequestBody UpdateBoardRequest request) {

        // TODO: 없는 id 에 대한 exception handling
        Board updateBoard = boardService.update(id, request);

        return ResponseEntity.ok()
                .body(new BoardResponse(updateBoard));
    }

    @DeleteMapping("/boards/{id}")
    public ResponseEntity<Void> deleteBoard(@PathVariable Long id) {
        // TODO: 없는 id 에 대한 exception handling
        boardService.delete(id);

        return ResponseEntity.ok()
                .build();
    }

}
