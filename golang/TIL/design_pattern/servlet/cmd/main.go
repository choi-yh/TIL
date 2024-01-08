package main

import (
	"fmt"
	"net"
	"os"

	"github.com/choi-yh/TIL/TIL/design_pattern/servlet/handler"
)

func main() {
	addr, err := net.ResolveTCPAddr("tcp4", ":9999")
	if err != nil {
		fmt.Printf("failed to resolve addr: %v\n", err)
		os.Exit(1)
	}

	listener, err := net.Listen("tcp4", addr.String())
	if err != nil {
		fmt.Printf("failed listen: %v\n", err)
		return
	}

	for {
		conn, err := listener.Accept()
		if err != nil {
			fmt.Printf("failed to accept: %v\n", err)
			continue
		}

		go handler.HandleRequest(conn)
	}
}
