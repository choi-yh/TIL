class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0

        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
            elif nums[left] != val:
                cnt += 1
                left += 1
            elif nums[right] == val:
                right -= 1
                
        return cnt


        
                