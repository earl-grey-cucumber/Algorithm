class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        len, count, start = 1, 9, 1
        while n > len * count:
            n -= len * count
            len += 1
            start *= 10
            count *= 10
        start += (n - 1) / len
        s = str(start)
        return int(s[(n - 1) % len])
	