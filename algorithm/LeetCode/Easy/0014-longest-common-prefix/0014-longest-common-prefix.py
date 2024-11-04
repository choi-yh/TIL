class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = min(map(len, strs))
        lcp = ""
        for i in range(n):
            t = strs[0][i]
            for s in strs:
                if s[i] != t:
                    return lcp

            lcp += t

        return lcp