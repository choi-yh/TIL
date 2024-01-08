package handler

import (
	"errors"
	"fmt"
	"io"
	"net"
	"net/http"
	"strings"

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
	method, path := parseRequestLine(request)
	fmt.Printf("request = %v\n", request)

	switch method {
	case "GET":
		HandleGETRequest(conn, path)
	case "POST":
		HandlePOSTRequest(conn, request)
	case "PUT":
		HandlePUTRequest(conn, request)
	case "DELETE":
		HandleDELETERequest(conn, path)
	default:
		internal.WriteErrorResponse(conn, http.StatusMethodNotAllowed, http.StatusText(http.StatusMethodNotAllowed))
	}

	conn.Close()
}

func parseRequestLine(request string) (string, string) {
	s := strings.Split(request, "\r\n")

	var httpInfos []string
	for _, v := range s {
		if strings.Contains(v, "HTTP") {
			httpInfos = strings.Split(v, " ")
			break
		}
	}

	return httpInfos[0], httpInfos[1]
}
