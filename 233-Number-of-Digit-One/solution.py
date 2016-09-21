class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        cur, base, result = n, 1, 0
        while cur > 0:
            digit = cur % 10
            cur /= 10
            result += cur * base
            if digit == 1:
                result += n % base + 1
            elif digit > 1:
                result += base
            base *= 10
        return result
 