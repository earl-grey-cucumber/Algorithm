class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        while n > 0:
            digit = n % 26 if n % 26 != 0 else 26
            result += chr(digit + ord('A') - 1)
            n = (n - digit) / 26
        return result[::-1]