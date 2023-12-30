package main

import (
	"fmt"
	"io"
	"net"
	"net/http"
	"os"
	"strings"

	"github.com/pkg/errors"
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

		go handleRequest(conn)
	}
}

func handleRequest(conn net.Conn) {
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

	if method == "GET" {
		if path == "/hello" {
			writeResponse(conn, "Hello World")
		} else {
			writeErrorResponse(conn, http.StatusNotFound, "")
		}
	} else if method == "POST" {
		contentType := parseRequestContentsType(request)
		if !checkJSONContentType(contentType) {
			writeErrorResponse(conn, http.StatusMethodNotAllowed, "Content-Type is mismatched")
			conn.Close()
		}

		contents := parseRequestContents(request)

		processRequestBody(contents)

		//writeResponse(conn, "POST request received")
		writeResponse(conn, contents)
	} else {
		writeErrorResponse(conn, http.StatusMethodNotAllowed, http.StatusText(http.StatusMethodNotAllowed))
	}

	conn.Close()
}

func checkJSONContentType(contentType string) bool {
	return contentType == "application/json"
}

func parseRequestContentsType(request string) string {
	s := strings.Split(request, "\r\n")
	for _, v := range s {
		if strings.Contains(v, "Content-Type") {
			ss := strings.Split(v, ": ")
			return ss[1]
		}
	}

	return ""
}

func processRequestBody(contents string) {
	fmt.Printf("Request body = %v", contents)
}

func parseRequestContents(request string) string {
	s := strings.Split(request, "\r\n\r\n")

	return s[1]
}

func writeErrorResponse(conn net.Conn, found int, message string) {
	fmt.Fprintf(conn, "HTTP/1.1 %d %s\r\n", found, http.StatusText(found))

	if len(message) != 0 {
		fmt.Fprintf(conn, message)
	} else {
		fmt.Fprintf(conn, "Content-Type: text/plain\r\n")
	}
}

func writeResponse(conn net.Conn, s string) {
	fmt.Fprintf(conn, "HTTP/1.1 %d %s\r\n", http.StatusOK, http.StatusText(http.StatusOK))
	fmt.Fprintf(conn, s)
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
