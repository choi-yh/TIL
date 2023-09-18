# https://www.acmicpc.net/problem/9935

def bomb_seq(seq, bomb):
    stack = []
    for text in seq:
        stack.append(text)
        if text == bomb[-1] and len(stack) >= len(bomb):
            remove_stack = []
            for _ in range(len(bomb)):
                remove_stack.append(stack.pop())
            if remove_stack[::-1] != bomb:
                stack.extend(remove_stack[::-1])
    
    if stack:
        return ''.join(stack)
    else:
        return "FRULA"


seq = list(input())
bomb = list(input())
print(bomb_seq(seq, bomb))
