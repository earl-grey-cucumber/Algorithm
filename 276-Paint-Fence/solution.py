class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return k
        same = k
        dif = k * (k - 1)
        for i in range(3, n + 1):
            temp = dif
            dif = dif * (k - 1) + same * (k - 1)
            same = temp
        return same + dif