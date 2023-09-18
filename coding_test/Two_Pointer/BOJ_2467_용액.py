# https://www.acmicpc.net/problem/2467


def get_solutions():
    start, end = 0, N - 1

    answer = [solutions[start], solutions[N - 1]]
    compound = abs(solutions[start] + solutions[N - 1])

    while start < end:
        cur_compound = solutions[start] + solutions[end]
        if abs(cur_compound) < compound:
            compound = abs(cur_compound)
            answer = [solutions[start], solutions[end]]

        if cur_compound < 0:
            start += 1
        else:
            end -= 1

    return answer


N = int(input())
solutions = list(map(int, input().split()))
print(*get_solutions())
