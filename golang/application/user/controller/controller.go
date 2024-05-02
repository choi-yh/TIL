package controller

import (
	"context"

	"github.com/choi-yh/TIL/golang/application/buf/gen/go/proto/user/v1"
	"github.com/choi-yh/TIL/golang/application/user/model"
	"github.com/choi-yh/TIL/golang/application/user/service"
	"google.golang.org/grpc"
	"google.golang.org/protobuf/types/known/timestamppb"
)

type Server struct {
	user_v1.UnimplementedUserServiceServer
	svc service.Service
}

func RegisterServer(srv *grpc.Server) {
	user_v1.RegisterUserServiceServer(srv, &Server{
		svc: service.NewService(),
	})
}

func (s *Server) SignUp(ctx context.Context, request *user_v1.SignUpRequest) (*user_v1.SignUpResponse, error) {
	user, err := s.svc.SignUp(ctx, model.SignUpParam{
		Email:    request.Email,
		Password: request.Password,
		Name:     request.Name,
		Phone:    request.Phone,
	})
	if err != nil {
		return nil, err
	}

	return &user_v1.SignUpResponse{
		User: &user_v1.User{
			Id:        int32(user.ID),
			Email:     user.Email,
			Name:      user.Name,
			Phone:     user.Phone,
			CreatedAt: timestamppb.New(user.CreatedAt),
		},
	}, nil
}

func (s *Server) Login(ctx context.Context, request *user_v1.LoginRequest) (*user_v1.LoginResponse, error) {

	return &user_v1.LoginResponse{}, nil
}
