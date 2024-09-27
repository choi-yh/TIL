package com.example.jump2springboot.answer;

import com.example.jump2springboot.question.Question;
import com.example.jump2springboot.question.QuestionService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@RequestMapping("/question/{question_id}")
@Controller
public class AnswerController {

    private final QuestionService questionService;
    private final AnswerService answerService;

    public AnswerController(QuestionService questionService, AnswerService answerService) {
        this.questionService = questionService;
        this.answerService = answerService;
    }

    @PostMapping("/answer")
    public String answer(Model model
            , @PathVariable("question_id") Integer id
            , @RequestParam("content") String content) {

        Question question = this.questionService.getQuestion(id);

        this.answerService.create(question, content);

        return String.format("redirect:/question/%d", question.getId());
    }
}
