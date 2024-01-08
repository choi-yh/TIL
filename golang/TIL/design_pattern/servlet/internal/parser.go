package internal

import (
	"strconv"
	"strings"
)

type RequestHeader struct {
	Method                  string
	Path                    string
	Version                 string
	Host                    string
	Connection              string
	SecChUa                 string
	SecChUaMobile           string
	SecChUaPlatform         string
	UpgradeInsecureRequests string
	UserAgent               string
	Accept                  string
	SecFetchSite            string
	SecFetchMode            string
	SecFetchUser            string
	SecFetchDest            string
	AcceptEncoding          string
	AcceptLanguage          string
	Cookie                  string
	ContentType             string
	ContentLength           int

	Contents string
}

func ParseRequestLine(request string) RequestHeader {
	requestLines := strings.Split(request, "\r\n")

	var httpInfos []string
	var header RequestHeader
	for _, v := range requestLines {
		if strings.Contains(v, "HTTP") {
			httpInfos = strings.Split(v, " ")
			header.Method, header.Path, header.Version = httpInfos[0], httpInfos[1], httpInfos[2]
		}

		s := strings.Split(v, ": ")
		switch s[0] {
		case "Host":
			header.Host = s[1]
		case "Connection":
			header.Connection = s[1]
		case "sec-ch-ua":
			header.SecChUa = s[1]
		case "sec-ch-ua-mobile":
			header.SecChUaMobile = s[1]
		case "sec-ch-ua-platform":
			header.SecChUaPlatform = s[1]
		case "Upgrade-Insecure-Requests":
			header.UpgradeInsecureRequests = s[1]
		case "User-Agent":
			header.UserAgent = s[1]
		case "Accept":
			header.Accept = s[1]
		case "Sec-Fetch-Site":
			header.SecFetchSite = s[1]
		case "Sec-Fetch-User":
			header.SecFetchUser = s[1]
		case "Sec-Fetch-Dest":
			header.SecFetchDest = s[1]
		case "Accept-Encoding":
			header.AcceptEncoding = s[1]
		case "Accept-Language":
			header.AcceptLanguage = s[1]
		case "Cookie":
			header.Cookie = s[1]
		case "Content-Type":
			header.ContentType = s[1]
		case "Content-Length":
			i, err := strconv.Atoi(s[1])
			if err != nil {
				i = 0
			}
			header.ContentLength = i
		}
	}

	s := strings.Split(request, "\r\n\r\n")
	header.Contents = s[1]

	return header
}

// 0 = {string} "GET /hello.do HTTP/1.1"
// 1 = {string} "Host: localhost:9999"
// 2 = {string} "Connection: keep-alive"
// 3 = {string} "sec-ch-ua: "Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120""
// 4 = {string} "sec-ch-ua-mobile: ?0"
// 5 = {string} "sec-ch-ua-platform: "macOS""
// 6 = {string} "Upgrade-Insecure-Requests: 1"
// 7 = {string} "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
// 8 = {string} "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
// 9 = {string} "Sec-Fetch-Site: none"
// 10 = {string} "Sec-Fetch-Mode: navigate"
// 11 = {string} "Sec-Fetch-User: ?1"
// 12 = {string} "Sec-Fetch-Dest: document"
// 13 = {string} "Accept-Encoding: gzip, deflate, br"
// 14 = {string} "Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,en-ZA;q=0.6,en-NZ;q=0.5,en-GB;q=0.4,en-AU;q=0.3,en-IN;q=0.2,en-CA;q=0.1,la;q=0.1"
// 15 = {string} "Cookie: Goland-fb2bf0c6=fc1b2a1d-2348-4e44-9539-61d7baca2d64"
// 16 = {string} ""
// 17 = {string} ""

// POST /hello HTTP/1.1
// Content-Type: application/json
// User-Agent: PostmanRuntime/7.36.0
// Accept: */*
// Postman-Token: 4fa3ec87-b468-4412-8a70-92defafdde0b
// Host: localhost:9999
// Accept-Encoding: gzip, deflate, br
// Connection: keep-alive
// Content-Length: 30
//
// {
//     "value": "hello world"
// }
