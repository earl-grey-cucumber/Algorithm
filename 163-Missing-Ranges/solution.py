class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        pre, i = lower - 1, 0
        result = []
        while i <= len(nums):
            val = nums[i] if i < len(nums) else upper + 1
            if val > pre + 1:
                if  pre + 1 == val - 1:
                    result.append(str(pre + 1))
                else:
                    result.append(str(pre + 1) + "->" + str(val - 1))
            pre = val
            i += 1
        return result
                