# https://www.acmicpc.net/problem/1197

def get_parent(parents, x):
    if parents[x] == x:
        return x

    return get_parent(parents, parents[x])


def union_find(parents, a, b):
    a_parent = get_parent(parents, a)
    b_parent = get_parent(parents, b)

    if a_parent < b_parent:
        parents[b_parent] = a_parent
    else:
        parents[a_parent] = b_parent

    return parents


def mst(v, graph):
    graph = sorted(graph, key=lambda x: x[2])

    answer = 0
    parents = [i for i in range(v + 1)]
    for a, b, c in graph:
        a_parent = get_parent(parents, a)
        b_parent = get_parent(parents, b)

        if a_parent != b_parent:
            parents = union_find(parents, a, b)
            answer += c

    return answer


V, E = map(int, input().split())
Graph = [list(map(int, input().split())) for _ in range(E)]
print(mst(V, Graph))
