class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        """
        dp = [sys.maxint for i in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        return dp[amount] if dp[amount] != sys.maxint else -1
        """
        dp = [0] + [sys.maxint] * amount 
        for i in range(amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i],dp[i - coin] + 1)
        return dp[amount] if dp[amount] != sys.maxint else -1
