# https://www.acmicpc.net/problem/10799
"""
레이저가 나올 때, 현재 포함된 막대기의 개수만큼 추가,
막대기가 끝나면 한조각 더 추가
"""

brackets = input()
answer = 0

stack = []
for i, b in enumerate(brackets):
    if b == "(":
        stack.append([b, i])
    else:
        tmp = stack.pop()
        if i - tmp[1] == 1:
            answer += len(stack)
        else:
            answer += 1
            
print(answer)