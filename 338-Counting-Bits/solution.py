class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0 for i in range(num + 1)]
        if num == 0:
            return dp
        dp[1] = 1
        for i in range(2, num + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp