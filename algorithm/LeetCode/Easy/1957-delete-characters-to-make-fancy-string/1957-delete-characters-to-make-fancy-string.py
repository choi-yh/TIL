class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        fancy = s[:2]
        for i in range(2, len(s)):
            if s[i] != fancy[-2] or fancy[-1] != fancy[-2]:
                fancy += s[i]

        return fancy