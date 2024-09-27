package com.example.jump2springboot;

import com.example.jump2springboot.question.Question;
import com.example.jump2springboot.question.QuestionRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;

@SpringBootTest
class Jump2springbootApplicationTests {

    @Autowired
    private QuestionRepository questionRepository;

    @Test
    void create() {
        Question q1 = new Question();
        q1.setTitle("sbb가 무엇인가요?");
        q1.setContent("sbb에 대해서 알고 싶습니다.");
        q1.setCreatedAt(LocalDateTime.now());
        this.questionRepository.save(q1);  // 첫번째 질문 저장

        Question q2 = new Question();
        q2.setTitle("스프링부트 모델 질문입니다.");
        q2.setContent("id는 자동으로 생성되나요?");
        q2.setCreatedAt(LocalDateTime.now());
        this.questionRepository.save(q2);  // 두번째 질문 저장
    }

    @Test
    void findAll() {
        List<Question> questionList = this.questionRepository.findAll();
        assertEquals(2, questionList.size());

        Question q = questionList.get(0);
        assertEquals("sbb가 무엇인가요?", q.getTitle());
    }

    @Test
    void findById() {
        // 값이 존재하지 않을 수 있기 때문에 Optional 을 사용.
        Optional<Question> question = this.questionRepository.findById(1);
        if (question.isPresent()) { // Optional 에서 값을 확인하기 위해 isPresent() 사용.
            Question q = question.get();
            assertEquals("sbb가 무엇인가요?", q.getTitle());
        }
    }

    @Test
    void findByTitle() {
        Question q = this.questionRepository.findByTitle("sbb가 무엇인가요?");
        assertEquals(1, q.getId());
    }
}
