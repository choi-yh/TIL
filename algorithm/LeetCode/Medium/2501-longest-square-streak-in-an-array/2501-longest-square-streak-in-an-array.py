class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        """
        1. 정렬한 뒤에
        2. 제곱한 값을 추가한 배열을 해당 인덱스에 추가
        """
        square_subseqs = [set() for _ in range(max(nums) + 1)]

        nums.sort()
        for num in nums:
            square_subseqs[num].add(num)

            square_num = num**2
            if square_num < len(square_subseqs):
                square_subseqs[square_num].update(square_subseqs[num])

        answer = 1
        for subseq in square_subseqs:
            if len(subseq) > answer:
                answer = len(subseq)

        if answer == 1:
            return -1

        return answer
