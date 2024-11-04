class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0

        max_value = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            if prices[i] > max_value:
                max_value = prices[i]
            else:
                answer = max(answer, max_value - prices[i])

        return answer
