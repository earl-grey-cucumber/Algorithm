class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n, k = len(s1), len(s2), len(s3)
        if m + n != k:
            return False
        dp = [False for j in range(n + 1)]
        dp[0] = True
        for j in range(1, n + 1):
            dp[j] = True if dp[j - 1] and s2[j - 1] == s3[j - 1] else False
        for i in range(1, m + 1):
            dp[0] = True if dp[0] and s1[i - 1] == s3[i - 1] else False
            for j in range(1, n + 1):
                if s1[i - 1] == s3[i + j - 1] and dp[j]:
                    dp[j] = True
                elif s2[j - 1] == s3[i + j - 1] and dp[j - 1]:
                    dp[j] = True
                else:
                    dp[j] = False
        return dp[n]