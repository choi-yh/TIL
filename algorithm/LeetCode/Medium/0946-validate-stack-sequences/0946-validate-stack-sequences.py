class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) < len(popped):
            return False

        stack = []
        pushed_idx, popped_idx = 0, 0
        n, m = len(pushed), len(popped)

        while pushed_idx < n and popped_idx < m:
            stack.append(pushed[pushed_idx])
            pushed_idx += 1

            while stack and popped_idx < m and stack[-1] == popped[popped_idx]:
                stack.pop()
                popped_idx += 1

        if stack:
            return False

        return True