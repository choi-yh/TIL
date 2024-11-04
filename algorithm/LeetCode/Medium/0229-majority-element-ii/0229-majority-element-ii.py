class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        answer = set()

        n = len(nums) / 3
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
            if dic[num] > n:
                answer.add(num)

        return list(answer)
