# https://www.acmicpc.net/problem/9009


def fibonacci(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp


def check(n):
    answer = []
    while n:
        for i in range(len(fibo)):
            if fibo[i] <= n:
                target = fibo[i]
            else:
                break
        n -= target
        answer.append(target)
    return answer[::-1]


t = int(input())
fibo = fibonacci(50)
print(fibo)
for _ in range(t):
    n = int(input())
    answer = check(n)
    print(" ".join(map(str, answer)))
