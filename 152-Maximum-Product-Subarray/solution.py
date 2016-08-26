class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        global_max, local_max = nums[0], nums[0]
        local_min = nums[0]
        for i in xrange(1, len(nums)):
            temp = local_max
            local_max = max(nums[i], local_max * nums[i], local_min * nums[i])
            local_min = min(nums[i], local_min * nums[i], temp * nums[i])
            global_max = max(local_max, global_max)
        return global_max
            
            