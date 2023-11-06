package main

import (
	"context"
	"fmt"
	"io"
	"log"
	"math/rand"
	"net/http"
	"strconv"
)

func rolldice(w http.ResponseWriter, r *http.Request) {
	ctx, span := tracer.Start(r.Context(), "rolldice-span")
	defer span.End()

	childRolldice(ctx)

	roll := 1 + rand.Intn(6)

	resp := strconv.Itoa(roll) + "\n"
	if _, err := io.WriteString(w, resp); err != nil {
		log.Printf("Write failed: %v\n", err)
	}
}

func childRolldice(ctx context.Context) {
	_, childSpan := tracer.Start(ctx, "childRolldice")
	defer childSpan.End()

	fmt.Printf("child Rolldice")
}
