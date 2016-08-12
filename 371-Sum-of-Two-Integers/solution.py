class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)
        """
        mask = 0xffffffff
        max_int = 0x7fffffff
        while b != 0:
            a = (a ^ b) & mask
            b = ((a & b) << 1) & mask
        return a if a <= max_int else ~(a ^ mask)
        """
        
       