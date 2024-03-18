package main

import "time"

type (
	Article struct {
		ID        int       `json:"id"`
		Title     string    `json:"title"`
		Body      string    `json:"body"`
		Published time.Time `json:"published"`
		Author    Author    `json:"author"`
	}

	Author struct {
		FirstName string `json:"first_name"`
		LastName  string `json:"last_name"`
	}
)

func (a Article) GetIndex() string {
	return "article"
}
