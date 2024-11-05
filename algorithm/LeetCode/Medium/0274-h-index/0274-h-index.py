class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # h 개의 논문을 선정했을 때, 인용 횟수가 h 번 이상인 h 중 최댓값.
        citations.sort(reverse=True)

        h = 0
        for i in range(1, len(citations) + 1):
            if citations[i - 1] >= i:
                h = i 

        return h
            

