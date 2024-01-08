package handler

import (
	"fmt"
	"net"
	"net/http"

	"github.com/choi-yh/TIL/TIL/design_pattern/servlet/internal"
)

func HandlePOSTRequest(conn net.Conn, header internal.RequestHeader) {
	if !checkJSONContentType(header.ContentType) {
		internal.WriteErrorResponse(conn, http.StatusMethodNotAllowed, "Content-Type is mismatched")
		return
	}

	switch header.Path {

	}

	//processRequestBody(contents)
	internal.WriteResponse(conn, header.Contents)
	return
}

func checkJSONContentType(contentType string) bool {
	return contentType == "application/json"
}

func processRequestBody(contents string) {
	fmt.Printf("Request body = %v", contents)
}
