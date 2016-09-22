class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        data = [1] + [i for i in nums if i > 0] + [1]
        n = len(data)
        dp = [[0]*n for _ in xrange(n)]
        for k in xrange(2, n):
            for left in xrange(0, n - k):
                right = left + k
                for i in xrange(left + 1,right):
                    dp[left][right] = max(dp[left][right],
                        data[left] * data[i] * data[right] + dp[left][i] + dp[i][right])
        return dp[0][n - 1]