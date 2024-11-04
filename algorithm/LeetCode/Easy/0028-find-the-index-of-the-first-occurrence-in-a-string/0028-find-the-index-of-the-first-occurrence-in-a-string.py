class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0] and i + len(needle) <= len(haystack) and haystack[i: i + len(needle)] == needle:
                return i

        return -1