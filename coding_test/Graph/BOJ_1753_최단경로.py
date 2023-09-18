# https://www.acmicpc.net/problem/1753

import heapq
import sys

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    node1, node2, dist = map(int, input().split())
    graph[node1].append([node2, dist])

# print(graph)

distances = {i: sys.maxsize for i in range(v + 1)}  # 시작점으로부터의 거리
distances[k] = 0

heap = []
heapq.heappush(heap, [distances[k], k])

while heap:
    dist, cur_node = heapq.heappop(heap)

    if distances[cur_node] < dist:
        continue

    for near_node, near_dist in graph[cur_node]:
        weighted_dist = dist + near_dist
        if distances[near_node] > weighted_dist:
            distances[near_node] = weighted_dist
            heapq.heappush(heap, [weighted_dist, near_node])

for i in range(1, v + 1):
    res = distances[i]
    if res == sys.maxsize:
        print("INF")
    else:
        print(distances[i])
