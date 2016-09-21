class Solution(object):
    def canCross(self, stones):
        lookup = {}
        for k, v in enumerate(stones):
            lookup[v] = k
        dp = [False for _ in xrange(len(stones))]
        dp[0] = True
        for i in xrange(len(stones)):
            if dp[i]:
                for k in (i-1, i, i+1):
                    if stones[i] + k in lookup:
                        dp[lookup[stones[i] + k]] = True
        return dp[-1]