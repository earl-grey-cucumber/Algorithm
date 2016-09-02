class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num > 0 and num % 2 == 0:
            num /= 2
        while num > 0 and num % 3 == 0:
            num /= 3
        while num > 0 and num % 5 == 0:
            num /= 5
        return num == 1