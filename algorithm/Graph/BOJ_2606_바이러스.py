# https://www.acmicpc.net/problem/2606

from collections import deque

def bfs(n, graph):
    q = deque()
    q.append(1)
    
    visited = [False] * (n + 1)
    visited[1] = True

    while q:
        cur_node = q.popleft()

        for next_node in graph[cur_node]:
            if visited[next_node] == False:
                q.append(next_node)
                visited[next_node] = True

    print(sum(visited) - 1)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(n, graph)