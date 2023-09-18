# https://www.acmicpc.net/problem/1105
"""
반례) [1280 1281], [1887 1888], [128 138]
"""


def eight():
    if len(L) < len(R):
        return 0
    elif L == R:
        return L.count("8")
    else:
        cnt = 0
        for i in range(len(L)):
            if L[i] == R[i] == "8":
                cnt += 1
            elif L[i] != R[i]:
                break

        return cnt


L, R = input().split()
print(eight())
