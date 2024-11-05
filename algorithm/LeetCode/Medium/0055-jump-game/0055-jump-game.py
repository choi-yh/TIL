class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums == [0]:
            return True

        if nums[0] == 0:
            return False

        dp = [False] * len(nums)
        dp[0] = True

        for i in range(len(nums)):
            if dp[i]:
                n = min(i + nums[i] + 1, len(nums))
                dp[i: n] = [True] * (n - i)
            
        return dp[-1]
