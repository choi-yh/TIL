class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer = 0
        n = math.ceil(len(nums) / 2)
        
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
            if dic[num] >= n:
                answer = num

        return answer