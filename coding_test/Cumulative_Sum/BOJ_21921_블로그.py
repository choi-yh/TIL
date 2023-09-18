# https://www.acmicpc.net/problem/21921

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

max_visit = sum(visitors[:x])
cur_sum = max_visit
cnt = 1

for i in range(x, len(visitors)):
    cur_sum += visitors[i] - visitors[i-x]
    if max_visit < cur_sum:
        max_visit = cur_sum
        cnt = 1
    elif max_visit == cur_sum:
        cnt += 1

if max_visit == 0:
    print("SAD")
else:
    print(max_visit)
    print(cnt)