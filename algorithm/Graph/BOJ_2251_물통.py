# https://www.acmicpc.net/problem/2251

from collections import deque
from itertools import permutations


water = list(map(int, input().split()))
answer = set()
moves = list(permutations(range(3), 2))

queue = deque()
queue.append([0, 0, water[2]])

visit = []
visit.append([0, 0, water[2]])

while queue:
    status = queue.popleft()
    if status[0] == 0:
        answer.add(status[2])

    for start, end in moves:
        new_status = status[:]
        moving_water = min(
            water[end] - status[end],  # 받을 수 있는 최대량
            status[start],  # 줄 수 있는 최대량
        )
        new_status[start] -= moving_water
        new_status[end] += moving_water
        if new_status not in visit:
            queue.append(new_status)
            visit.append(new_status)

print(" ".join(list(map(str, sorted(answer)))))
