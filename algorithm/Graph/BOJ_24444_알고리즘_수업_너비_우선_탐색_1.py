# https://www.acmicpc.net/problem/24444

import sys
from collections import deque

def bfs(n, m, r, graph):
    order = 1

    visited = [0] * (n+1)
    visited[r] = order

    q = deque()
    q.append(r)
    while q:
        cur_node = q.popleft()
        for next_node in graph[cur_node]:
            if visited[next_node] == 0:
                order += 1
                visited[next_node] = order
                q.append(next_node)

    print(*visited[1:], sep="\n")

n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
graph = [sorted(node) for node in graph]

bfs(n, m, r, graph)
