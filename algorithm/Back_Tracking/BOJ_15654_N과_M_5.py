# https://www.acmicpc.net/problem/15654

import sys
from itertools import permutations

def get_sequence(n, m, arr):
    for seq in list(permutations(arr, m)):
        print(' '.join(list(map(str, seq))))

n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))

get_sequence(n, m, arr)