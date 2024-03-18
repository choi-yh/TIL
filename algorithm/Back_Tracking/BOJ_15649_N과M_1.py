# https://www.acmicpc.net/problem/15649

from itertools import permutations

n, m = map(int, input().split())
result = list(permutations(list(range(1, n+1)), m))
for comb in result:
    for n in comb:
        print(n, end=' ')
    print('')
