class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last_idx = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c in seen:
                continue

            while stack and c < stack[-1] and i < last_idx[stack[-1]]:
                seen.discard(stack.pop())

            stack.append(c)
            seen.add(c)

        return "".join(stack)
