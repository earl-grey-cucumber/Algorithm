class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dp = [False for _ in xrange(len(stones))]
        dp[0] = True
        if stones[1] - stones[0] == 1:
            dp[1] = True
        #if len(stones) == 2:
        #   return dp[-1]
        for i in xrange(2, len(stones)):
            for j in reversed(xrange(i)):
                if stones[i] - stones[j] > j + 1:
                    break
                if dp[j] and ((stones[i] - stones[j]) in [j-1, j, j+1]):
                    dp[i] = True
                    break
        return dp[-1]