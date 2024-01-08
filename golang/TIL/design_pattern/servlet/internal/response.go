package internal

import (
	"fmt"
	"net"
	"net/http"
)

func WriteErrorResponse(conn net.Conn, found int, message string) {
	fmt.Fprintf(conn, "HTTP/1.1 %d %s\r\n", found, http.StatusText(found))
	fmt.Fprintf(conn, "Server: dante-server\r\n")

	fmt.Fprintf(conn, "\n")
	if len(message) != 0 {
		fmt.Fprintf(conn, message)
	} else {
		fmt.Fprintf(conn, "Content-Type: text/plain\r\n")
	}
}

func WriteResponse(conn net.Conn, s string) {
	fmt.Fprintf(conn, "HTTP/1.1 %d %s\r\n", http.StatusOK, http.StatusText(http.StatusOK))
	fmt.Fprintf(conn, "Server: dante-server\r\n")
	fmt.Fprintf(conn, "Content-Length: %d\r\n", len(s))

	fmt.Fprintf(conn, "\n")
	fmt.Fprintf(conn, s)
}
