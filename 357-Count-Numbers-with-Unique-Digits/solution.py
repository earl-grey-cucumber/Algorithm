class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        if n < 0:
            return 0
        if n == 0:
            return 1
        dp = [1, 9] + [0] * (9 - 1)
        result = dp[0] + dp[1]
        if n == 1:
            return result
        for i in range(2, n + 1):
            if 9 - i + 2 > 1:
                dp[i] = dp[i - 1] * (9 - i + 2)
            else:
                break
            result += dp[i]
        return result