# https://www.acmicpc.net/problem/2023


def check_prime(num):
    if num == 0 or num == 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def amazing_prime(num):
    if check_prime(num):
        if len(str(num)) == n:
            print(num)
            return

        for i in range(1, 10):
            amazing_prime(num * 10 + i)


n = int(input())
for num in range(1, 10):
    amazing_prime(num)
