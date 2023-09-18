# https://www.acmicpc.net/problem/1644

def get_primes(n):
    sieve = [True] * (n + 1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, n + 1, i):
                sieve[j] = False

    return [i for i in range(2, n + 1) if sieve[i]]


def get_continuous_sum(target, primes):
    answer = 0
    left, right = 0, 0

    while right <= len(primes):
        cur_sum = sum(primes[left:right])

        if cur_sum == target:
            answer += 1
            right += 1
        elif cur_sum < target:
            right += 1
        else:
            left += 1

    return answer


N = int(input())
P = get_primes(N)
print(get_continuous_sum(N, P))
