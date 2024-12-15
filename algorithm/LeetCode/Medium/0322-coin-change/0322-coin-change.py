class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [inf] * (amount + 1)
        for coin in coins:
            if coin > amount:
                continue

            dp[coin] = 1
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] != inf else -1