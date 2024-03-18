# https://www.algospot.com/judge/problem/read/BRACKETS2

"""
여는 부분을 스택에 넣고, 
닫는 부분이 나올 때 스택에서 하나씩 꺼내서 매칭 시키기
"""

brackets = {
    "(": ")",
    "{": "}",
    "[": "]"
}

c = int(input())  # test_case

for _ in range(c):
    formula = input()
    stack = []
    for bracket in formula:
        # 여는 부분일 경우 스택에 추가
        if bracket in brackets.keys():
            stack.append(bracket)
        else:
            if len(stack) == 0:
                stack.append(bracket)
                break
            elif brackets[stack[-1]] != bracket:
                stack.append(bracket)
                break
            else:
                stack.pop()

    if len(stack) == 0:
        print("YES")
    else:
        print("NO")