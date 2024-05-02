package handler

import (
	"net"
	"net/http"
	"os"

	"github.com/choi-yh/TIL/golang/TIL/design_pattern/servlet/internal"
)

func HandleGETRequest(conn net.Conn, path string) {
	switch path {
	case "/hello":
		internal.WriteResponse(conn, "Hello World")
	case "/hello.do":
		// FIXME: Need to change the way files are read
		b, err := os.ReadFile("/Users/younghyo/Projects/TIL/golang/TIL/design_pattern/servlet/hello.html")
		if err != nil {
			internal.WriteErrorResponse(conn, http.StatusInternalServerError, err.Error())
		}
		html := string(b)

		internal.WriteResponse(conn, html)
	default:
		internal.WriteErrorResponse(conn, http.StatusNotFound, "")
	}
}
