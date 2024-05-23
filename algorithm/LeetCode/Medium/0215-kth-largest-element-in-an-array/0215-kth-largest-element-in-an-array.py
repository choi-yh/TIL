class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)
        sorted_nums = sorted(list(nums), reverse=True)
        return sorted_nums[k-1]