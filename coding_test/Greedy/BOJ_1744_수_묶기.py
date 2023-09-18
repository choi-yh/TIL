# https://www.acmicpc.net/problem/1744

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

negative = sorted([num for num in array if num <= 0])
positive = sorted([num for num in array if num > 0], reverse=True)

answer = 0
while len(positive) > 1:
    first, second, *others = positive
    answer += max(first * second, first + second)

    positive = others

while len(negative) > 1:
    first, second, *others = negative
    answer += max(first * second, first + second)

    negative = others

if positive:
    answer += positive[0]
if negative:
    answer += negative[0]

print(answer)
