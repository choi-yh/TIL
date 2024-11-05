class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(len(nums)):
            j = 1
            while i + j < len(nums) and j <= nums[i]:
                dp[i + j] = dp[i] + 1 if dp[i + j] == 0 else min(dp[i + j], dp[i] + 1)
                j += 1

        return dp[-1]