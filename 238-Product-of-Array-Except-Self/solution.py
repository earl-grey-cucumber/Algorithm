class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre, suf, n = 1, 1, len(nums)
        result = [1 for i in range(n)]
        for i, num in enumerate(nums):
            result[i] *= pre
            result[n - 1 - i] *= suf
            pre *= nums[i]
            suf *= nums[n - 1 - i]
        return result