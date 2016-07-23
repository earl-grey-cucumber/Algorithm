class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        dp = [True] * n
        i = 2
        while i * i < n:
            if dp[i]:
                j = i
                while j * i < n:
                    dp[j * i] = False
                    j += 1
            i += 1
        count = 0
        for i in range(2, n):
            if dp[i]:
                count += 1
        return count
            
        