# https://www.acmicpc.net/problem/11000

import heapq

n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]
classes = sorted(classes, key=lambda x: x[0])

rooms = []
for start_time, end_time in classes:
    if not rooms:
        rooms.append(end_time)
    else:
        cur_time = heapq.heappop(rooms)
        if start_time >= cur_time:
            heapq.heappush(rooms, end_time)
        else:
            heapq.heappush(rooms, cur_time)
            heapq.heappush(rooms, end_time)

print(len(rooms))
