package internal

import (
	"fmt"
	"net"
	"net/http"
)

func WriteErrorResponse(conn net.Conn, found int, message string) {
	fmt.Fprintf(conn, "HTTP/1.1 %d %s\r\n", found, http.StatusText(found))
	fmt.Fprint(conn, "Server: dante-server\r\n")

	fmt.Fprint(conn, "\n")
	if len(message) != 0 {
		fmt.Fprint(conn, message)
	} else {
		fmt.Fprint(conn, "Content-Type: text/plain\r\n")
	}
}

func WriteResponse(conn net.Conn, s string) {
	fmt.Fprintf(conn, "HTTP/1.1 %d %s\r\n", http.StatusOK, http.StatusText(http.StatusOK))
	fmt.Fprint(conn, "Server: dante-server\r\n")
	fmt.Fprintf(conn, "Content-Length: %d\r\n", len(s))

	fmt.Fprint(conn, "\n")
	fmt.Fprint(conn, s)
}
