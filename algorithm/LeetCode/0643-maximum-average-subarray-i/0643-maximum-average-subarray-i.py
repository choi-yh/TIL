class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ = sum(nums[:k])
        answer = summ / k
        for i in range(k, len(nums)):
            summ = summ - nums[i - k] + nums[i]
            answer = max(answer, summ / k)

        return answer