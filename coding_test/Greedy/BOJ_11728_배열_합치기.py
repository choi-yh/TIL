# https://www.acmicpc.net/problem/11728

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(" ".join(map(str, sorted(a + b))))