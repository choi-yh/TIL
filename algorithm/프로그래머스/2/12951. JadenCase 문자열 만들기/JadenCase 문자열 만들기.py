def solution(s):
    stack = []
    for i in range(len(s)):
        if len(stack) == 0 or stack[-1] == " ":
            stack.append(s[i].upper())
        else:
            stack.append(s[i].lower())
    
    return ''.join(stack)