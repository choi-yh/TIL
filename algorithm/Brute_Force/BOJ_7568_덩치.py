# https://www.acmicpc.net/problem/7568

def get_build_rank(n, builds):
    result = [1] * n
    for i, build in enumerate(builds):
        for j in range(n):
            if build[0] < builds[j][0] and build[1] < builds[j][1]:
                result[i] += 1
    
    return result

n = int(input())
builds = [list(map(int, input().split())) for _ in range(n)]
result = get_build_rank(n, builds)

print(' '.join(map(str, result)))