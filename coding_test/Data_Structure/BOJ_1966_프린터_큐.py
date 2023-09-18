# https://www.acmicpc.net/problem/1966


def printer(docs, indices):
    answer = []

    while docs:
        doc = docs.pop(0)
        idx = indices.pop(0)

        if len(docs) == 0:
            answer.append(idx)
        elif doc >= max(docs):
            answer.append(idx)
        else:
            docs.append(doc)
            indices.append(idx)

    return answer


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))
    indices = list(range(n))
    print(printer(docs, indices).index(m) + 1)
