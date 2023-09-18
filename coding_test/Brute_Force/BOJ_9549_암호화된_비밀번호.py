# https://www.acmicpc.net/problem/9549
from collections import Counter


def check(t, p):
    p_counter = Counter(p)
    t_counter = Counter(t[:len(p)])
    t_counter[t[len(p) - 1]] -= 1

    for i in range(len(t) - len(p) + 1):
        t_counter[t[i + len(p) - 1]] += 1

        if t_counter == p_counter:
            return "YES"
        else:
            t_counter[t[i]] -= 1
            if t_counter[t[i]] == 0:
                del t_counter[t[i]]

    return "NO"


T = int(input())
for _ in range(T):
    target = input()
    password = input()

    print(check(target, password))
