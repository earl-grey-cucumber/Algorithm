class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def helper(n):
            result = 0
            while n > 0:
                result += (n % 10) ** 2
                n /= 10
            return result
        if n <= 0:
            return False
        visited =  set()
        while n != 1:
            if n in visited:
                return False
            visited.add(n)
            n = helper(n)
        return True

            