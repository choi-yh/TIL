# https://www.acmicpc.net/problem/9237

def cal_invite_day(trees):
    answer = 0
    for i, tree in enumerate(trees):
        answer = max(answer, i + tree)

    print(answer + 2)


N = int(input())
T = sorted(list(map(int, input().split())), reverse=True)

cal_invite_day(T)
