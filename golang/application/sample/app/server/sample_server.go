package server

import (
	"context"
	"fmt"

	sample "github.com/choi-yh/TIL/application/sample/protos/sample"
)

type SampleServer struct {
	sample.SampleServiceServer
}

func (s *SampleServer) Echo(ctx context.Context, request *sample.StringMessage) (*sample.StringMessage, error) {
	return &sample.StringMessage{Value: request.Value}, nil
}

func (s *SampleServer) SayHello(ctx context.Context, request *sample.HelloRequest) (*sample.HelloResponse, error) {
	helloMessage := fmt.Sprintf("Hello %s", request.Name)
	return &sample.HelloResponse{Message: helloMessage}, nil
}
