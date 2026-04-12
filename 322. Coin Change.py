class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if min(coins) > amount:
            return -1
        if amount in coins:
            return 1
        dp = [10**10] * (amount+1)
        for i in range(len(coins)):
            if coins[i] < amount:
                dp[coins[i]] = 1
        for i in range(len(dp)):
            for k in coins:
                if i-k >= 0:
                    dp[i] = min(dp[i], dp[i-k]+1)
            if i == amount:
                if dp[amount] == 10**10:
                    return -1
                return dp[amount]
        if dp[amount] == 10**10:
            return -1
        else:
            return dp[amount]
