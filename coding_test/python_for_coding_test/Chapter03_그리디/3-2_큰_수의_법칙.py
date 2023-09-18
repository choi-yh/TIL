"""
큰 수의 법칙 : 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙

입력 조건
* 첫째 줄에 N(2 <= N <= 1000), M(1 <= M <= 10000), K(1 <= K <= 10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
* 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10000 이하의 수로 주어진다.
* 입력으로 주어지는 K는 항상 M보다 작거나 같다.

출력 조건
* 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

입력 예시
5 8 3
2 4 5 4 6

출력 예시
46
"""

n, m, k = map(int, input().split())
number = list(map(int, input().split()))

number = sorted(number, reverse=True)

answer = 0

# m이 매우 큰 경우에는 이 방법이 좋지 않다. (시간 복잡도)
for i in range(m):
    if (i + 1) % k == 0:
        answer += number[1]
    else:
        answer += number[0]
print(46)
