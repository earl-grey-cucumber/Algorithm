class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        maps = {}
        for i in range(len(nums)):
            if nums[i] in maps and i - maps[nums[i]] <= k:
                return True
            maps[nums[i]] = i
        return False