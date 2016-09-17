class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        if x + y < z:
            return False
        elif x + y == z:
            return True
        else:
            return z % gcd(x, y) == 0
            