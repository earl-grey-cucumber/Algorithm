class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = self._dp
        while len(dp) <= n:
            cur = sys.maxint
            for i in range(1, int(len(dp)**0.5+1)):
                cur = min(dp[-i*i], cur)
            dp += [cur + 1]
        return dp[n]
        """
        if n <= 0:
            return 0
        dp = [0] + [sys.maxint] * n
        for i in range(1, n + 1):
            j = 1
            while i >= j * j:
                dp[i] = min(dp[i - j * j] + 1, dp[i])
                j += 1
        return dp[n]
        """
        