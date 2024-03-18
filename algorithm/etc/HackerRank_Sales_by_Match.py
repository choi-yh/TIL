# https://www.hackerrank.com/challenges/sock-merchant/problem

from collections import Counter


def sockMerchant(n, ar):
    answer = 0
    counts = Counter(ar)
    print(counts)

    for cnt in counts.values():
        answer += cnt // 2
    return answer


print(sockMerchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]))
