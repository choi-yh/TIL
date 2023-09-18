# https://www.acmicpc.net/problem/16120

def check_ppap(t):
    stack = []
    for s in t:
        if len(stack) > 3:
            if ''.join(stack[-4:]) == "PPAP":
                stack[-4:] = "P"
        stack.append(s)

    if ''.join(stack) == "PPAP" or stack == ["P"]:
        print("PPAP")
    else:
        print("NP")


check_ppap(list(input()))
