# https://www.acmicpc.net/problem/24479

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(r):
    visited[r] = True
    order.append(r)
    
    for next_node in graph[r]:
        if visited[next_node] == False:
            dfs(next_node)
    
    return

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
graph = [sorted(node) for node in graph]

visited = [False] * (n+1)
visited[r] = True
order = [0]

dfs(r)

result = [0] * (n+1)
for i, o in enumerate(order):
    result[o] = i
    
for i in range(1, n+1):
    print(result[i])