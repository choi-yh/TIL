package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var (
	reader = bufio.NewReader(os.Stdin)
	writer = bufio.NewWriter(os.Stdin)
	maxInt = math.MaxInt64
)

func dijkstra(graph [][]int, start, end, n int) int {
	visited := make([]bool, n+1)
	visited[start] = true

	dist := make([]int, n+1)
	for i := 0; i < n+1; i++ {
		dist[i] = maxInt
	}

	for i, d := range graph[start] {
		if d > 0 {
			dist[i] = d
		}
	}
	dist[start] = 0

	for i := 0; i < n; i++ {
		curIdx := getMinIdx(dist, visited)
		visited[curIdx] = true
		for nextNode, d := range graph[curIdx] {
			if !visited[nextNode] && d > 0 {
				dist[nextNode] = int(math.Min(float64(dist[nextNode]), float64(d+dist[curIdx])))
			}
		}
	}

	return dist[end]
}

func getMinIdx(dist []int, visited []bool) int {
	target := 0
	distance := maxInt
	for i, d := range dist {
		if d < distance && !visited[i] {
			target = i
			distance = d
		}
	}

	return target
}

func main() {
	defer writer.Flush()

	var n, e int
	fmt.Fscanln(reader, &n, &e)

	graph := make([][]int, n+1)
	for i := 0; i < n+1; i++ {
		graph[i] = make([]int, n+1)
	}

	for i := 0; i < e; i++ {
		var a, b, c int
		fmt.Fscanln(reader, &a, &b, &c)

		if graph[a][b] > 0 {
			c = int(math.Min(float64(graph[a][b]), float64(c)))
		}

		graph[a][b] = c
		graph[b][a] = c
	}

	var v1, v2 int
	fmt.Fscanln(reader, &v1, &v2)

	oneToV1 := dijkstra(graph, 1, v1, n)
	oneToV2 := dijkstra(graph, 1, v2, n)

	v1ToV2 := dijkstra(graph, v1, v2, n)

	v1ToN := dijkstra(graph, v1, n, n)
	v2ToN := dijkstra(graph, v2, n, n)

	road1 := oneToV1 + v1ToV2 + v2ToN
	road2 := oneToV2 + v1ToV2 + v1ToN

	answer := int(math.Min(float64(road1), float64(road2)))
	if answer < 0 {
		fmt.Println(-1)
		return
	}

	fmt.Println(answer)
}
