package main

import (
	"github.com/choi-yh/TIL/golang/application/server"
)

func main() {
	apiServer := server.NewAPIServer()
	go apiServer.Run()

	grpcServer := server.NewGrpcServer()
	grpcServer.Run()
}
