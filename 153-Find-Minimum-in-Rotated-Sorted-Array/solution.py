class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        cand = nums[0]
        while low <= high:
            mid = low + (high - low) / 2
            if nums[low] <= nums[mid]:
                cand = min(cand, nums[low])
                low = mid + 1
            else:
                cand = min(cand, nums[mid])
                high = mid - 1
        return cand
            