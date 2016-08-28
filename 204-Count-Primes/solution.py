class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [True for i in range(n)] # True means is prime number
        i = 2
        while i * i < n:
            if dp[i]:
                temp = i * i
                while temp < n:
                    dp[temp] = False
                    temp += i
            i += 1            
        count = 0
        for i in range(2, n):
            if dp[i]:
                count += 1
        return count