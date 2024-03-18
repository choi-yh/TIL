# https://www.acmicpc.net/problem/5904
# 참고) https://tesseractjh.tistory.com/101

import sys
sys.setrecursionlimit(10 ** 9)

def moo(n, k, s_k):
    s_k_i = (s_k - (k+3)) // 2 # s(k-1)의 길이
    
    # 왼쪽 s(k-1)에서 찾는 경우, s(k-1)에서 찾는 것과 같은 결과
    if n <= s_k_i:
        return moo(n, k-1, s_k_i)
    
    # 오른쪽 s(k-1)에서 찾아야 하는 경우, 오른쪽 파트에 맞춰 n 과 s_k_i 계산
    elif n > s_k_i + (k+3):
        return moo(n - (s_k_i + k+3), k-1, s_k_i)
    
    # 가운데 파트에서 찾는 경우, 첫 글자 인덱스 확인
    else: 
        if n == s_k_i + 1:
            return "m"
        else:
            return "o"

n = int(sys.stdin.readline())
s_k, k = 3, 0
while n > s_k:
    k += 1
    s_k = 2 * s_k + (k + 3) # s(k)의 총 길이
    
print(moo(n, k, s_k))
