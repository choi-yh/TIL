class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        lps = ""
        n = len(s)
        for i in range(n - 1):
            # 홀수개
            substring = s[i]
            left, right = i - 1, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                substring = s[left] + substring + s[right]
                left -= 1
                right += 1

            if len(lps) < len(substring):
                lps = substring

            # 짝수개
            substring = ""
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                substring = s[left] + substring + s[right]
                left -= 1
                right += 1

            if len(lps) < len(substring):
                lps = substring

        return lps
