class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result, temp = 0, 5
        while n >= temp:
            result += n / temp
            temp *= 5
        return result