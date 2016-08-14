class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for num in nums:
            xor ^= num
        temp = xor & ~(xor - 1)  #111 & 001 = 001 110 & 010 = 010 only leave last non-0 bit
        cand1, cand2 = 0, 0
        for num in nums:
            if num & temp != 0:
                cand1 ^= num
            else:
                cand2 ^= num
        return [cand1, cand2]
