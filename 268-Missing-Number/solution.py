class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, xor = len(nums), 0
        for num in nums:
            xor ^= num
        for i in range(n + 1):
            xor ^= i
        return xor