class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for t in s:
            if t != "*":
                stack.append(t)
            else:
                stack.pop()

        return "".join(stack)