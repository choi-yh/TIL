package server

import (
	"context"
	"fmt"

	"github.com/choi-yh/TIL/golang/application/sample/protos/sample"
)

type SampleServer struct {
	sample.UnimplementedSampleServiceServer
}

func (s *SampleServer) Echo(ctx context.Context, request *sample.StringMessage) (*sample.StringMessage, error) {
	return &sample.StringMessage{Value: request.GetValue()}, nil
}

func (s *SampleServer) SayHello(ctx context.Context, request *sample.HelloRequest) (*sample.HelloResponse, error) {
	helloMessage := fmt.Sprintf("Hello %s", request.GetName())
	return &sample.HelloResponse{Message: helloMessage}, nil
}
