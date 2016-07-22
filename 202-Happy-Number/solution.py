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
        slow, fast = n, n
        while fast != 1:
            fast = convert(fast)
            if fast == 1:
                return True
            slow = convert(slow)
            fast = convert(fast)
            if slow == fast:
                return False
        return True
        