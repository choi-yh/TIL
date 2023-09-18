# https://www.acmicpc.net/problem/2531


def max_sushi():
    answer = 0
    for i in range(N):
        if i > N - k:
            dishes = sushi[i:N] + sushi[:k - N + i]
        else:
            dishes = sushi[i:i + k]

        dishes.append(c)
        comb = set(dishes)

        answer = max(answer, len(comb))

    return answer


N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
print(max_sushi())
