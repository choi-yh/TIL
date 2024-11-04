class Solution:
    def isPalindrome(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if ord("a") <= ord(s[i].lower()) <= ord("z") or ord('0') <= ord(s[i]) <= ord('9'):
                stack.append(s[i].lower())

        if len(stack) % 2 == 0:
            return stack[:len(stack) // 2] == stack[len(stack) // 2:][::-1]
        else:
            return stack[:len(stack) // 2 + 1] == stack[len(stack) // 2:][::-1]