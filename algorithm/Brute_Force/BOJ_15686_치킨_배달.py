# https://www.acmicpc.net/problem/15686

from itertools import combinations


def chicken_distance(house, chicken):
    return abs(chicken[0] - house[0]) + abs(chicken[1] - house[1])


n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
chickens = [[i, j] for i in range(n) for j in range(n) if city[i][j] == 2]
houses = [[i, j] for i in range(n) for j in range(n) if city[i][j] == 1]

chicken_cases = list(combinations(range(len(chickens)), m))

check = 99999
for remain_chickens in chicken_cases:
    answer = 0
    for house in houses:
        dist = 999
        for chicken_index in remain_chickens:
            dist = min(dist, chicken_distance(house, chickens[chicken_index]))
        answer += dist
    check = min(check, answer)
    
print(check)