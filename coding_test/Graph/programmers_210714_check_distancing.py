# https://programmers.co.kr/learn/courses/30/lessons/81302


def check_room(room):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    # 모든 자리 확인
    for i in range(5):
        for j in range(5):
            if room[i][j] == "P":
                stack = []
                visit = []
                stack.append([i, j])
                while stack:
                    cur_pos = stack.pop()
                    x, y = cur_pos[0], cur_pos[1]
                    visit.append([x, y])
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if (
                            (nx >= 0 and nx < 5 and ny >= 0 and ny < 5)
                            and room[nx][ny] != "X"
                            and [nx, ny] not in visit
                            and abs(i - nx) + abs(j - ny) <= 2
                        ):
                            if room[nx][ny] == "P":
                                return False
                            else:
                                stack.append([nx, ny])
    return True


def solution(places):
    answer = []
    for room in places:
        room = [list(people for people in row) for row in room]
        if check_room(room):
            answer.append(1)
        else:
            answer.append(0)

    return answer
