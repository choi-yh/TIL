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
	maxInt = 999999999
)

func dijkstra(graph [][]int, start, end, n int) []int {
	visited := make([]bool, n)
	visited[start] = true

	dist := make([]int, n)
	for i := 0; i < n; i++ {
		dist[i] = graph[start][i]
	}

	for i := 0; i < n; i++ {
		curIdx := getMinIdx(dist, visited)
		visited[curIdx] = true
		for j, cost := range graph[curIdx] {
			if !visited[j] {
				dist[j] = int(math.Min(float64(dist[j]), float64(dist[curIdx]+cost)))
			}
		}
	}

	return dist
}

func getMinIdx(dist []int, visited []bool) int {
	idx := 0
	minVal := maxInt
	for i := 0; i < len(dist); i++ {
		if dist[i] < minVal && !visited[i] {
			minVal = dist[i]
			idx = i
		}
	}

	return idx
}

func main() {
	defer writer.Flush()

	var n, m int
	fmt.Fscanln(reader, &n)
	fmt.Fscanln(reader, &m)

	graph := make([][]int, n)
	for i := 0; i < n; i++ {
		graph[i] = make([]int, n)
	}

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if i != j {
				graph[i][j] = maxInt
			}
		}
	}

	for i := 0; i < m; i++ {
		var s, e, dist int
		fmt.Fscanln(reader, &s, &e, &dist)
		s--
		e--

		graph[s][e] = int(math.Min(float64(dist), float64(graph[s][e])))
	}

	var start, end int
	fmt.Fscanln(reader, &start, &end)

	dist := dijkstra(graph, start-1, end-1, n)
	fmt.Println(dist[end-1])
}
