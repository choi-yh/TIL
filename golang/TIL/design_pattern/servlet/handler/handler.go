package handler

import (
	"errors"
	"fmt"
	"io"
	"net"
	"net/http"

	"github.com/choi-yh/TIL/TIL/design_pattern/servlet/internal"
)

func HandleRequest(conn net.Conn) {
	buf := make([]byte, 1024)

	n, err := conn.Read(buf)
	if err != nil {
		if errors.Is(err, io.EOF) {
			return
		}
		fmt.Print(err.Error())
	}

	request := string(buf[:n])
	header := internal.ParseRequestLine(request)
	fmt.Printf("request = \n%v\n", header)

	switch header.Method {
	case "GET":
		HandleGETRequest(conn, header.Path)
	case "POST":
		HandlePOSTRequest(conn, request)
	case "PUT":
		HandlePUTRequest(conn, request)
	case "DELETE":
		HandleDELETERequest(conn, header.Path)
	default:
		internal.WriteErrorResponse(conn, http.StatusMethodNotAllowed, http.StatusText(http.StatusMethodNotAllowed))
	}

	conn.Close()
}
