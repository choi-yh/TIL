package com.example.jump2springboot.answer;

import com.example.jump2springboot.question.Question;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;

@Service
public class AnswerService {

    private final AnswerRepository answerRepository;

    public AnswerService(AnswerRepository answerRepository) {
        this.answerRepository = answerRepository;
    }

    public void create(Question question, String content) {
        Answer answer = new Answer();
        answer.setContent(content);
        answer.setCreatedAt(LocalDateTime.now());
        answer.setQuestion(question);
        this.answerRepository.save(answer);
    }
}
