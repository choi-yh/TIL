# https://www.acmicpc.net/problem/1325

import sys
from collections import deque

def bfs(graph, start, n):
    q = deque([start])
    visited = [False] * (n+1)
    visited[start] = True
    cnt = 0

    while q:
        cur_node = q.popleft()
        for next_node in graph[cur_node]:
            if visited[next_node] == False:
                visited[next_node] = True
                q.append(next_node)
                cnt += 1
                
    return cnt

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

result = []
max_cnt = 0
for i in range(1, n+1):
    cnt = bfs(graph, i, n)
    if cnt > max_cnt:
        max_cnt = cnt
    result.append([i, cnt])
    
for i, cnt in result:
    if cnt == max_cnt:
        print(i, end=' ')