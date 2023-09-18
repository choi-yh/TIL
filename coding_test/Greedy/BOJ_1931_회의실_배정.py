# https://www.acmicpc.net/problem/1931


n = int(input())
meetings = sorted(
    [list(map(int, input().split())) for _ in range(n)], key=lambda x: [x[1], x[0]]
)
answer = 0
flag = 0
for meet_start, meet_end in meetings:
    if flag <= meet_start:
        answer += 1
        flag = meet_end

print(answer)
