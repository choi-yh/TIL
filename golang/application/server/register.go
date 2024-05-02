package server

import (
	user "github.com/choi-yh/TIL/golang/application/user/controller"
	"google.golang.org/grpc"
)

func Register(srv *grpc.Server) {
	user.RegisterServer(srv)
}
