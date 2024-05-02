package main

import (
	"github.com/choi-yh/TIL/golang/application/sample/app"
	"github.com/choi-yh/TIL/golang/application/sample/app/server"
)

func main() {
	grpcGateway := app.NewGrpcGateway()
	go grpcGateway.Run()

	grpcServer := server.NewGrpcServer()
	grpcServer.Run()
}
