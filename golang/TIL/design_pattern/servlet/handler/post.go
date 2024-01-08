package handler

import (
	"fmt"
	"net"
	"net/http"
	"strings"

	"github.com/choi-yh/TIL/TIL/design_pattern/servlet/internal"
)

func HandlePOSTRequest(conn net.Conn, request string) {
	contentType := parseRequestContentsType(request)
	if !checkJSONContentType(contentType) {
		internal.WriteErrorResponse(conn, http.StatusMethodNotAllowed, "Content-Type is mismatched")
		return
	}

	contents := parseRequestContents(request)
	//processRequestBody(contents)
	internal.WriteResponse(conn, contents)
	return
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

func checkJSONContentType(contentType string) bool {
	return contentType == "application/json"
}

func parseRequestContents(request string) string {
	s := strings.Split(request, "\r\n\r\n")

	return s[1]
}

func processRequestBody(contents string) {
	fmt.Printf("Request body = %v", contents)
}
