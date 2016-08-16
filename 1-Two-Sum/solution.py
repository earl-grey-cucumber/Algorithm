class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        maps = {}
        for i, num in enumerate(nums):
            if target - num in maps:
                return maps[target - num], i
            maps[num] = i
        return -1, -1