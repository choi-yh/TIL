class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashmap = dict()
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        print(hashmap)
        res = 1
        while hashmap.get(res, 0) > 0:
            res += 1

        return res