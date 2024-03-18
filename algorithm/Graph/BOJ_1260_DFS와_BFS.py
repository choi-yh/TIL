# https://www.acmicpc.net/problem/1260

from collections import deque

n, m, v = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

def dfs(graph, start):
    graph = [sorted(node, reverse=True) for node in graph] # 정점 번호가 작은 곳을 먼저 방문하기 위해 내림차순 정렬
    stack = [start]
    visit = []
    
    while stack:
        cur_node = stack.pop()
        if cur_node not in visit:
            visit.append(cur_node)
            stack.extend(graph[cur_node])
    return visit

def bfs(graph, start):
    queue = deque()
    visit = []
    queue.append(start)
    while queue:
        cur_node = queue.popleft()
        if cur_node not in visit:
            visit.append(cur_node)
            queue.extend(graph[cur_node])
    return visit

def solve(n, m, v, edges):
    graph = [[] for _ in range(n+1)]
    for node1, node2 in edges:
        graph[node1].append(node2)
        graph[node2].append(node1)
    graph = [sorted(node) for node in graph]
    
    return " ".join(map(str, dfs(graph, v))) + "\n" + " ".join(map(str, bfs(graph, v)))

print(solve(n, m, v, edges))

if __name__ == "__main__":
    # test1
    n1, m1, v1 = 4, 5, 1
    edges1 = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]]
    
    # test2
    n2, m2, v2 = 5, 5, 3
    edges2 = [[5, 4], [5, 2], [1, 2], [3, 4], [3, 1]]
    
    # test3
    n3, m3, v3 = 1000, 1, 1000
    edges3 = [[999, 1000]]
    
    print(solve(n1, m1, v1, edges1))
    print(solve(n2, m2, v2, edges2))