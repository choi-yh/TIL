# https://www.acmicpc.net/problem/1541

def lost_bracket():
    stack = []

    flag = False
    for t in text:
        if t == "-":
            if flag is False:
                flag = True
                stack.append("-")
                stack.append("(")
            else:
                flag = True
                stack.append(")")
                stack.append("-")
                stack.append("(")
        else:
            if len(stack) == 0 and t == "0":
                pass
            else:
                if t != "0":
                    stack.append(t)
                elif stack[-1] in ["-", "+", "(", ")"] and t == "0":
                    pass
                else:
                    stack.append(t)

    if flag is True:
        stack.append(")")

    if len(stack) == 0:
        stack.append('0')

    return eval("".join(stack))


text = input()
print(lost_bracket())
