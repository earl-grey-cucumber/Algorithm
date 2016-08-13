class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two = 0, 0
        for num in nums:
            two |= num & one
            one ^= num
            three = two & one
            one = (~three) & one
            two = (~three) & two
        return one