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
	maxInt = 100001
)

type NextPos struct {
	cur, left, right, double int
}

func getNextPos(curIdx int) NextPos {
	return NextPos{
		cur:    curIdx,
		left:   curIdx - 1,
		right:  curIdx + 1,
		double: 2 * curIdx,
	}
}

func bfs(start int) []int {
	dist := make([]int, maxInt)
	for i := 0; i < len(dist); i++ {
		dist[i] = maxInt
	}
	dist[start] = 0

	curIdx := start
	next := getNextPos(curIdx)

	leftVisited := make(map[int]bool)
	rightVisited := make(map[int]bool)
	doubleVisited := make(map[int]bool)

	leftVisited[start], rightVisited[start], doubleVisited[start] = true, true, true

	var q []NextPos
	q = append(q, next)
	for len(q) > 0 {
		pos := q[0]
		q = q[1:]

		if pos.left >= 0 && !leftVisited[pos.left] {
			dist[pos.left] = int(math.Min(float64(dist[pos.left]), float64(dist[pos.cur]+1)))

			leftVisited[pos.left] = true
			q = append(q, getNextPos(pos.left))
		}

		if pos.right < maxInt && !rightVisited[pos.right] {
			dist[pos.right] = int(math.Min(float64(dist[pos.right]), float64(dist[pos.cur]+1)))

			rightVisited[pos.right] = true
			q = append(q, getNextPos(pos.right))
		}

		if pos.double < maxInt && !doubleVisited[pos.double] {
			dist[pos.double] = int(math.Min(float64(dist[pos.double]), float64(dist[pos.cur])))

			doubleVisited[pos.double] = true
			q = append(q, getNextPos(pos.double))
		}
	}

	return dist
}

func main() {
	defer writer.Flush()

	var n, k int
	fmt.Fscanln(reader, &n, &k)

	if n == k {
		fmt.Println(0)
		return
	}

	dist := bfs(n)

	fmt.Println(dist[k])
}
