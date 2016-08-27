class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val = nums[0]
        for num in nums:
            max_val = max(max_val, num)
        low, high = 1, max_val
        while low <= high:
            mid = low + (high - low) / 2
            if low == high:
                return low
            count = 0
            for i in range(len(nums)):
                if low <= nums[i] <= mid:
                    count += 1
            if count > mid - low + 1:
                high = mid
            else:
                low = mid + 1
        return low