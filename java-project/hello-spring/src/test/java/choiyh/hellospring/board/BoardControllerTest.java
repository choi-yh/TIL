package choiyh.hellospring.board;

import choiyh.hellospring.board.dto.AddBoardRequest;
import choiyh.hellospring.board.dto.UpdateBoardRequest;
import choiyh.hellospring.board.repository.BoardRepository;
import com.fasterxml.jackson.databind.ObjectMapper;
import jakarta.transaction.Transactional;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.ResultActions;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;
import org.springframework.web.context.WebApplicationContext;

import java.util.Arrays;
import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;
import static org.hamcrest.Matchers.hasSize;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;


@AutoConfigureMockMvc
@SpringBootTest
public class BoardControllerTest {

    @Autowired
    protected MockMvc mockMvc;

    @Autowired
    private WebApplicationContext context;

    @Autowired
    protected ObjectMapper objectMapper;

    @Autowired
    BoardRepository boardRepository;

    @BeforeEach
    public void setMockMvc() {
        this.mockMvc = MockMvcBuilders.webAppContextSetup(context)
                .build();
    }

    @BeforeEach
    public void cleanUp() {
        // TODO: 책에서 이렇게 진행을 하는데 테스트 실행 전 모든 DB 값을 삭제하게 됨.
        // 현재 테스트와 관련된 데이터만 사용하는 방법 찾아볼 것.
        boardRepository.deleteAll();
    }

    @Test
    public void addBoardTest() throws Exception {
        // given
        final String url = "/boards";
        final String title = "제목1";
        final String content = "본문2";
        final AddBoardRequest request = new AddBoardRequest(title, content);

        final String jsonBody = objectMapper.writeValueAsString(request);

        // when
        ResultActions result = mockMvc.perform(post(url)
                .content(jsonBody)
                .contentType(MediaType.APPLICATION_JSON));

        // then
        result.andExpect(status().isCreated());

        List<Board> boards = boardRepository.findAll();

        assertThat(boards.size()).isEqualTo(1);
        assertThat(boards.get(0).getTitle()).isEqualTo(title);
        assertThat(boards.get(0).getContent()).isEqualTo(content);
    }

    @Transactional
    @Test
    public void findAll() throws Exception {
        // given
        final String url = "/boards";
        int beforeSize = boardRepository.findAll().size();

        final Board board1 = Board.builder()
                .title("title1")
                .content("content1")
                .build();
        final Board board2 = Board.builder()
                .title("title2")
                .content("content2")
                .build();
        final Board board3 = Board.builder()
                .title("title3")
                .content("content3")
                .build();

        boardRepository.saveAll(Arrays.asList(board1, board2, board3));

        // when
        final ResultActions result = mockMvc.perform(get(url)
                .contentType(MediaType.APPLICATION_JSON));

        List<Board> allBoards = boardRepository.findAll();

        // then
        result
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.*", hasSize(beforeSize + 3)));

        assertThat(allBoards)
                .contains(board1)
                .contains(board2)
                .contains(board3);
    }

    @Transactional
    @Test
    public void getBoard() throws Exception {
        // given
        final String url = "/boards/{id}";

        final String title = "title";
        final String content = "content";
        final Board board = Board.builder()
                .title(title)
                .content(content)
                .build();

        boardRepository.save(board);

        Long wrongId = 0L;

        // when
        ResultActions normalResult = mockMvc.perform(get(url, board.getId())
                .contentType(MediaType.APPLICATION_JSON)
        );

        // then
        normalResult
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.title").value(title))
                .andExpect(jsonPath("$.content").value(content));
    }

    @DisplayName("update 성공 케이스")
    @Transactional
    @Test
    public void updateBoard() throws Exception {
        // given
        final String url = "/boards/{id}";

        final String title = "title";
        final String content = "content";
        final Board board = Board.builder()
                .title(title)
                .content(content)
                .build();

        boardRepository.save(board);

        final String updateTitle = "updated title";
        final String updateContent = "updated content";

        UpdateBoardRequest request = new UpdateBoardRequest(updateTitle, updateContent);

        // when
        // TODO: 없는 데이터에 대한 exception handling 케이스
        ResultActions result = mockMvc.perform(put(url, board.getId())
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(request)));

        // then
        result
                .andExpect(status().isOk());

        Board updatedBoard = boardRepository.findById(board.getId()).get();

        assertThat(updatedBoard.getTitle()).isEqualTo(updateTitle);
        assertThat(updatedBoard.getContent()).isEqualTo(updateContent);
    }

    @DisplayName("delete 성공 케이스")
    @Transactional
    @Test
    public void deleteBoard() throws Exception {
        // given
        final String url = "/boards/{id}";

        final String title = "title";
        final String content = "content";
        final Board board = Board.builder()
                .title(title)
                .content(content)
                .build();

        boardRepository.save(board);

        // when
        // TODO: 없는 id 삭제에 대한 exception handling
        ResultActions result = mockMvc.perform(delete(url, board.getId()));

        // then
        result
                .andExpect(status().isOk());
        assertThat(boardRepository.findById(board.getId())).isEmpty();
    }

}
