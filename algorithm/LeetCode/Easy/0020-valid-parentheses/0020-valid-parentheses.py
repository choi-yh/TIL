class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ["(", "{", "["]:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                elif s[i] == ")" and stack[-1] != "(":
                    return False
                elif s[i] == "}" and stack[-1] != "{":
                    return False
                elif s[i] == "]" and stack[-1] != "[":
                    return False

                stack.pop()
        
        if stack:
            return False
            
        return True