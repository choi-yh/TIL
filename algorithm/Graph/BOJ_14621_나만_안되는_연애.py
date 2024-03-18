# https://www.acmicpc.net/problem/14621


def get_parents(parents, x):
    if parents[x] != x:
        parents[x] = get_parents(parents, parents[x])
    return parents[x]


def kruskal(routes, genders, n):
    routes = sorted(routes, key=lambda x: x[2])
    parents = [i for i in range(n + 1)]

    distance = 0
    edges = 0
    for u, v, d in routes:
        u_parent = get_parents(parents, u)
        v_parent = get_parents(parents, v)
        if genders[u - 1] != genders[v - 1] and u_parent != v_parent:
            distance += d
            edges += 1
            if u_parent > v_parent:
                parents[u_parent] = v_parent
            else:
                parents[v_parent] = u_parent
        
    if edges == n - 1:
        return distance
    else:
        return -1


n, m = map(int, input().split())
genders = list(input().split())
routes = [list(map(int, input().split())) for _ in range(m)]
print(kruskal(routes, genders, n))
