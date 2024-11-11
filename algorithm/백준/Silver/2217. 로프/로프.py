n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort(reverse=True)

answer = 0
for i in range(n):
    answer = max(answer, ropes[i] * (i + 1))

print(answer)
