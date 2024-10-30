class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []

        for num in nums:
            if not lis or lis[-1] < num:
                lis.append(num)
            else:
                idx = self.bst(lis, num)
                lis[idx] = num

        return len(lis)

    def bst(self, lis: List[int], num: int) -> int:
        left, right = 0, len(lis) - 1
        while left <= right:
            mid = (left + right) // 2
            if lis[mid] < num:
                left = mid + 1
            elif lis[mid] > num:
                right = right - 1
            else:
                return mid
                
        return left
