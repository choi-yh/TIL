# https://www.acmicpc.net/problem/6603

import sys
from itertools import combinations

def lotto(k, s):
    case = list(combinations(s, 6))
    for c in case:
        print(' '.join(list(map(str, c))))
    
    print('')

while True:
    test_case = list(map(int, sys.stdin.readline().split()))
    if test_case[0] == 0:
        break
    
    k, s = test_case[0], test_case[1:]
    lotto(k, s)
    
if __name__ == "__main__":
    k, s = 7, [1, 2, 3, 4, 5, 6, 7]
    lotto(k, s)