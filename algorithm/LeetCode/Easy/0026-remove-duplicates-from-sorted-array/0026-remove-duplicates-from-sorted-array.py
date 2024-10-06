class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] = 999

        k = len(nums) - nums.count(999)
        nums.sort()

        return k