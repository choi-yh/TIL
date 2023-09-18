# https://www.acmicpc.net/problem/2643

def pile_paper(n, papers):
    papers = sorted(papers, key=lambda x: (x[0], x[1]))

    dp = [1] * n
    for i, paper in enumerate(papers):
        if i == 0:
            continue

        for j in range(i):
            if paper[1] >= papers[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


n = int(input())
p = [sorted(map(int, input().split())) for _ in range(n)]

print(pile_paper(n, p))
