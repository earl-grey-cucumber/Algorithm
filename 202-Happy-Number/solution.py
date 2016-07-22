class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def convert(n):
            result = 0
            while n > 0:
                d = n % 10
                result += d**2
                n /= 10
            return result
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            n = convert(n)
        return n == 1
        