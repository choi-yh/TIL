# https://www.acmicpc.net/problem/10974

import sys
from itertools import permutations

n = int(sys.stdin.readline())
for permutation in list(permutations(range(1, n+1), n)):
    print(' '.join(list(map(str, permutation))))