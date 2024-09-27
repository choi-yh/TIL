package com.example.jump2springboot.question;

import org.springframework.data.jpa.repository.JpaRepository;

public interface QuestionRepository extends JpaRepository<Question, Integer> {
    Question findByTitle(String title);
}
