# https://www.acmicpc.net/problem/1182

import sys
from itertools import combinations

def get_subsequence(n, s, arr):
    result = 0
    for i in range(1, n+1):
        for sub in list(combinations(arr, i)):
            if sum(sub) == s:
                result += 1
        
    return result

n, s = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
print(get_subsequence(n, s, arr))