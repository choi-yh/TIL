class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []

        dp = [False] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                dp[i] = True

        if len(nums) < k:
            return [-1] if all(dp) else [nums[-1]]

        for i in range(k, len(nums) + 1):
            subarray = nums[i - k : i]
            subdp = dp[i - k + 1 : i]
            if all(subdp):
                res.append(subarray[-1])
            else:
                res.append(-1)

        return res
