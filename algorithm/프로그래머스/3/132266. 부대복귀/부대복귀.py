"""
각 좌표간의 거리를 두고,
목적지 (destination) 에서 각 지점까지의 거리를 dijkstra 를 활용해서 계산한다.
sources 를 돌면서 정답 넣기
"""
import sys
from collections import defaultdict, deque

def solution(n, roads, sources, destination):
    answer = []
    
    road_map = defaultdict(list)
    for road in roads:
        road_map[road[0]].append(road[1])
        road_map[road[1]].append(road[0])
    
    dist = [sys.maxsize for _ in range(n + 1)]
    dist[destination] = 0
    
    dq = deque([destination])
    while dq:
        road = dq.popleft()
        for next_road in road_map[road]:
            if dist[next_road] > dist[road] + 1:
                dist[next_road] = dist[road] + 1
                dq.append(next_road)
    
    for s in sources:
        if dist[s] == sys.maxsize:
            answer.append(-1)
        else:
            answer.append(dist[s])
    
    return answer