class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(16):
            left, right = (n >> i) & 1, (n >> (31 - i)) & 1
            if left != right:
                n ^= (1 << (31 - i)) 
                n ^= (1 << i) 
        return n