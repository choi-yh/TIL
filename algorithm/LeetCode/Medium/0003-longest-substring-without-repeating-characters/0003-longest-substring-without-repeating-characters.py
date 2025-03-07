class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0

        n = len(s)
        for i in range(n):
            substring = set()
            for j in range(i, n):
                if s[j] in substring:
                    answer = max(answer, len(substring))
                    break
                substring.add(s[j])

                if j == n - 1:
                    answer = max(answer, len(substring))

        return answer