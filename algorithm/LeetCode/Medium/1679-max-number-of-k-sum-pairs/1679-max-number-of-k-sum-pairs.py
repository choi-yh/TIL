class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0

        hashmap = dict()
        for i in range(len(nums)):
            if nums[i] >= k:
                continue

            if hashmap.get(nums[i], 0) > 0:
                hashmap[nums[i]] -= 1
                res += 1
            else:
                hashmap[k - nums[i]] = hashmap.get(k - nums[i], 0) + 1

        return res
