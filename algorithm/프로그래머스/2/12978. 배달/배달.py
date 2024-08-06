import sys

def dijkstra(graph, start):
    dist = [sys.maxsize] * (len(graph) + 1)
    dist[start] = 0
    
    stack = [start]
    while stack:
        town = stack.pop()
        for next_town, d in graph[town]:
            if dist[next_town] > d + dist[town]:
                dist[next_town] = d + dist[town]
                stack.append(next_town)
                
    return dist

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)] 
    for r in road:
        src, dest, dist = r
        graph[src].append((dest, dist))
        graph[dest].append((src, dist))
        
    dist = dijkstra(graph, 1)

    answer = 0
    for d in dist:
        if d <= K:
            answer += 1
    
    return answer