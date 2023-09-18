# https://www.acmicpc.net/problem/9372

from collections import deque


def bfs(graph, start, visited, cnt):
    q = deque()
    q.append(start)
    visited.append(start)

    while q:
        cur_node = q.popleft()
        for next_node in graph[cur_node]:
            if next_node not in visited:
                q.append(next_node)
                visited.append(next_node)
                cnt += 1

    return cnt


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    g = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)

    print(bfs(g, 1, [], 0))
