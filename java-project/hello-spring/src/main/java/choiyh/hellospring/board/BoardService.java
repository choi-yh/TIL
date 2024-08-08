package choiyh.hellospring.board;

import choiyh.hellospring.board.dto.AddBoardRequest;
import choiyh.hellospring.board.dto.UpdateBoardRequest;
import jakarta.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@RequiredArgsConstructor // final 이 붙거나 @NotNull 이 붙은 필드의 생성자 추가
@Service
public class BoardService {

    @Autowired
    private final BoardRepository boardRepository;

    public Board save(AddBoardRequest request) {
        return boardRepository.save(request.toEntity());
    }

    public List<Board> findAll() {
        return boardRepository.findAll();
    }

    public Board findById(Long id) {
        return boardRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("not found: " + id));
    }

    @Transactional
    public Board update(Long id, UpdateBoardRequest request) {
        Board board = boardRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("not found: " + id));

        board.update(request.getTitle(), request.getContent());

        return board;
    }


    public void delete(Long id) {
        boardRepository.deleteById(id);
    }

}
