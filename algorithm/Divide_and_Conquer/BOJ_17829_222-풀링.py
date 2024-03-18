# https://www.acmicpc.net/problem/17829

import sys

sys.setrecursionlimit(10 ** 9)


def pooling(img):
    n = len(img)
    if n == 1:
        return img[0][0]

    new_img = []
    for i in range(0, n, 2):
        row = []
        for j in range(0, n, 2):
            row.append(sorted(list(img[i][j:j + 2] + img[i + 1][j:j + 2]), reverse=True)[1])
        new_img.append(row)

    return pooling(new_img)


N = int(input())
image = [list(map(int, input().split())) for _ in range(N)]
print(pooling(image))
