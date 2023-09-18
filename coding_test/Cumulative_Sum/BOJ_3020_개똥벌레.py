# https://www.acmicpc.net/problem/3020
# https://hongcoding.tistory.com/6

def count_destruction():
    min_count, range_count = N, 0

    # 길이가 긴 것부터 내려간다.
    for j in range(H - 1, 0, -1):
        bottom[j] += bottom[j + 1]
        top[j] += top[j + 1]

    for k in range(1, H + 1):
        if bottom[k] + top[H - k + 1] < min_count:
            min_count = bottom[k] + top[H - k + 1]
            range_count = 1
        elif bottom[k] + top[H - k + 1] == min_count:
            range_count += 1

    return [min_count, range_count]


N, H = map(int, input().split(" "))
top = [0] * (H + 1)
bottom = [0] * (H + 1)
for i in range(N):
    if i % 2 == 0:
        bottom[int(input())] += 1
    else:
        top[int(input())] += 1

print(*count_destruction())
