class Solution:
    def compress(self, chars: List[str]) -> int:
        target = chars[0]
        s = target

        start = 0
        for i in range(len(chars)):
            if chars[i] != target:
                if i - start > 1:
                    s += str(i - start)
                start = i
                target = chars[i]
                s += target

        if start < len(chars) - 1:
            s += str(i - start + 1)

        for i, v in enumerate(list(s)):
            chars[i] = v

        return len(s)
