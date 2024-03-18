# https://www.acmicpc.net/problem/4779

import sys

def cantor_set(n):
    if n == 1:
        return "-"
    
    partition = n // 3
    return cantor_set(partition) + " " * partition + cantor_set(partition)

while True:
    try:
        n = int(sys.stdin.readline())
        print(cantor_set(3 ** n))
    except:
        break