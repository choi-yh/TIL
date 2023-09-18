# https://www.acmicpc.net/problem/10971

import sys


def dfs(visit, total_cost):
    global answer

    cur_city = visit[-1]
    if len(visit) == n and cities[cur_city][visit[0]]:
        answer = min(answer, total_cost + cities[cur_city][visit[0]])
        return

    for near_city, cost in enumerate(cities[cur_city]):
        if near_city not in visit and cost and total_cost + cost < answer:
            visit.append(near_city)
            dfs(visit, total_cost + cost)
            visit.pop()


n = int(input())
cities = [list(map(int, input().split())) for _ in range(n)]

answer = sys.maxsize
for i in range(n):
    dfs([i], 0)

print(answer)
