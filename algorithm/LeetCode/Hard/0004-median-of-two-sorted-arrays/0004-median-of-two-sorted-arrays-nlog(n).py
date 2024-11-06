class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        
        merged_array = nums1 + nums2
        merged_array.sort() # nlog(n)

        mid = (m + n) // 2
        if (m + n) % 2 == 0:
            return (merged_array[mid - 1] + merged_array[mid]) / 2
        else:
            return float(merged_array[mid])