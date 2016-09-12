class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n - 1
        digit = n % 3
        if digit == 0:
            return pow(3, n / 3)
        elif digit == 1:
            return pow(3, (n - 4) / 3) * 4
        else:
            return pow(3, n/ 3) * 2