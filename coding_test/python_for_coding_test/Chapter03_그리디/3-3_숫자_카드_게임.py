# 2019 국가 교육기관 코딩 테스트
"""
입력 예시 1    출력 예시 1
3 3            2
3 1 2
4 1 4
2 2 2

입력 예시 2    출력 예시 2
2 4            3
7 3 1 8
3 3 3 4
"""

"""
입력되는 행마다 최솟값을 찾고,
그 행의 최솟값이 이전까지의 값보다 클 경우 업데이트 해준다.
"""
n, m = map(int, input().split())
answer = 0

for _ in range(n):
    cur_min = min(list(map(int, input().split())))

    if answer < cur_min:
        answer = cur_min

print(answer)
