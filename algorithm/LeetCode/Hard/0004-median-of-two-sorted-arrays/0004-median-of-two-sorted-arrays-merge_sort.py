class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        
        # merge_sort 에서의 병합 과정 (O(m + n))
        merged_array = []
        l, r = 0, 0
        while l < m and r < n:
            if nums1[l] < nums2[r]:
                merged_array.append(nums1[l])
                l += 1
            else:
                merged_array.append(nums2[r])
                r += 1

        merged_array += nums1[l:]
        merged_array += nums2[r:]

        mid = (m + n) // 2
        if (m + n) % 2 == 0:
            return (merged_array[mid - 1] + merged_array[mid]) / 2
        else:
            return float(merged_array[mid])