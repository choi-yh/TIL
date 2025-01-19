class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        answer = [0] * n

        a_set = set()
        b_set = set()
        for i, (a, b) in enumerate(zip(A, B)):
            a_set.add(a)
            b_set.add(b)

            answer[i] = len(a_set.intersection(b_set))

        return answer
