class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n - 1
        dp = [0, 1, 2, 3] + [0 for i in range(n - 3)]
        for i in range(4, n + 1):
            dp[i] = max(dp[i - 2] * 2, dp[i - 3] * 3)
        return dp[n]