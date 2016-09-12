class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        def count_1(n):
            count = 0
            while n:
                n = n & (n - 1)
                count += 1
            return count
        count = 0
        while n != 1:
            if n % 2 == 0:
                n /= 2
            elif n == 3 or count_1(n - 1) < count_1(n + 1):
                n -= 1
            else:
                n += 1
            count += 1
        return count