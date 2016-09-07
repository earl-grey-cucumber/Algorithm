class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 9
        if n == 1:
            return 10
        result = 10
        for i in range(2, n + 1):
            if 9 - i + 2 > 1:
                dp[i] = dp[i - 1] * (9 - i + 2)
                result += dp[i]
            else:
                break
        return result