# https://www.acmicpc.net/problem/11559

from collections import deque


def drop_puyo(delete_point, fields):
    for x, y in delete_point:  # 연쇄에 있는 뿌요 제거
        fields[x][y] = "."

    # 회전시켜서 끝으로 보내기
    rotated_fields = [[0] * 12 for _ in range(6)]
    for i in range(12):
        for j in range(6):
            rotated_fields[j][i] = fields[i][j]

    for i, row in enumerate(rotated_fields):
        if row.count(".") == 12:  # 더 내릴게 없는 상태
            continue
        else:
            stack = []
            for puyo in row:
                if puyo != ".":
                    stack.append(puyo)

            for _ in range(12 - len(stack)):
                stack.insert(0, ".")

            for j in range(12):
                fields[j][i] = stack[j]

    return fields


def find_puyo(fields):
    delete_point = []
    # 터지는 부분 찾기
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for x in range(11, -1, -1):
        for y in range(6):
            if [x, y] in delete_point or fields[x][y] == ".":
                continue

            q = deque()
            q.append([x, y])
            visit = []
            visit.append([x, y])
            puyo = fields[x][y]
            while q:  # BFS로 같은 뿌요 탐색
                x, y = q.popleft()
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if (
                        nx >= 0 and nx < 12 and ny >= 0 and ny < 6
                        and [nx, ny] not in visit
                        and fields[nx][ny] == puyo
                    ):
                        visit.append([nx, ny])
                        q.append([nx, ny])

            # 4개 이상이면 터트리기
            if len(visit) >= 4:
                delete_point.extend(visit)

    return delete_point


fields = [list(input()) for _ in range(12)]
chain = 0
while True:
    delete_point = find_puyo(fields)
    if not delete_point:
        break
    fields = drop_puyo(delete_point, fields)
    chain += 1

print(chain)
