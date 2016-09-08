class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0:
            return 0
        dp = [[sys.maxint, sys.maxint, sys.maxint] for i in range(n + 1)]
        dp[0] = [0, 0, 0]
        for i in range(1, n + 1):
            for j in range(3):
                for k in range(3):
                    if j != k:
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + costs[i - 1][j])
        return min(dp[n][0], dp[n][1], dp[n][2])
