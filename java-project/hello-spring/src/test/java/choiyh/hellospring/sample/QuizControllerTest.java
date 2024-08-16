package choiyh.hellospring.sample;

import com.fasterxml.jackson.databind.ObjectMapper;
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

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest
@AutoConfigureMockMvc
public class QuizControllerTest {

    @Autowired
    protected MockMvc mockMvc;

    @Autowired
    private WebApplicationContext context;

    @Autowired
    private ObjectMapper objectMapper; // Jackson 라이브러리에서 제공. 객체와 JSON 간의 변환을 처리해준다.

    @BeforeEach
    public void setMockMvc() {
        this.mockMvc = MockMvcBuilders.webAppContextSetup(context)
                .build();
    }


    @DisplayName("quiz(): GET /quiz?code=1 이면 응답 코드는 201, 응답 본문은 Created!를 리턴한다.")
    @Test
    public void getQuiz1() throws Exception {
        // given
        final String url = "/quiz";

        // when
        final ResultActions result = mockMvc.perform(get(url) // perform(): 요청을 전송하는 역할.
                .param("code", "1")
        );

        // then
        result
                .andExpect(status().isCreated())
                .andExpect(content().string("Created!"));
    }

    @DisplayName("quiz(): GET /quiz?code=2 이면 응답 코드는 400, 응답 본문은 Bad Request!를 리턴한다.")
    @Test
    public void getQuiz2() throws Exception {
        // given
        final String url = "/quiz";

        // when
        final ResultActions result = mockMvc.perform(get(url)
                .param("code", "2")
        );

        // then
        result
                .andExpect(status().isBadRequest())
                .andExpect(content().string("Bad Request!"));
    }

    @DisplayName("quiz(): POST /quiz?code=1 이면 응답 코드는 403, 응답 본문은 Forbidden!을 리턴한다.")
    @Test
    public void postQuiz1() throws Exception {
        // given
        final String url = "/quiz";
        QuizController.Code code = new QuizController.Code(1);
        // objectMapper.writeValueAsString() 사용하고, contentType 만 json 으로 보내줘도 괜찮다.
        byte[] content = objectMapper.writeValueAsBytes(code);

        // when
        ResultActions result = mockMvc.perform(post(url)
                .content(content)
                .contentType(MediaType.APPLICATION_JSON));

//        ResultActions result = mockMvc.perform(post(url)
//                .content(objectMapper.writeValueAsString(new QuizController.Code(1)))
//                .contentType(MediaType.APPLICATION_JSON));

        // then
        result
                .andExpect(status().isForbidden())
                .andExpect(content().string("Forbidden!"));
    }

    @DisplayName("quiz(): POST /quiz?code=13 이면 응답 코드는 200, 응답 본문은 OK!을 리턴한다.")
    @Test
    public void postQuiz2() throws Exception {
        // given
        final String url = "/quiz";
        QuizController.Code code = new QuizController.Code(13);
        byte[] content = objectMapper.writeValueAsBytes(code);

        // when
        ResultActions result = mockMvc.perform(post(url)
                .content(content)
                .contentType(MediaType.APPLICATION_JSON));

        // then
        result
                .andExpect(status().isOk())
                .andExpect(content().string("OK!"));
    }

}
