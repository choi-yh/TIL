# 2018 E 기업 알고리즘 대회
"""
입력 예시
25 5

출력 예시
2
"""

n, k = map(int, input().split())
answer = 0

while True:
    answer += 1
    if n % k != 0:
        n -= 1
    else:
        n = min(n - 1, n // k)

    if n == 1:
        break

print(answer)
