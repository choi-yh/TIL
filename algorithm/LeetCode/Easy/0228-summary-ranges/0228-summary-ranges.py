class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []

        if len(nums) == 0:
            return answer
        if len(nums) == 1:
            return [str(nums[0])]

        a, b = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i] == b + 1:
                b = nums[i]
            else:
                answer.append([a, b])

                a = nums[i]
                b = nums[i]
        
        answer.append([a, b])
        
        for i in range(len(answer)):
            if answer[i][0] == answer[i][1]:
                answer[i] = str(answer[i][0])
            else:
                answer[i] = "{}->{}".format(answer[i][0], answer[i][1])

        return answer
