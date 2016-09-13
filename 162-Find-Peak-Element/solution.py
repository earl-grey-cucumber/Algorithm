class Solution(object):
    def findPeakElement(self, nums):
        """
        n = len(nums)
        l, h = 0, n - 1
        while l <= h:
            mid = l + (h - l) / 2
            if mid - 1 >= 0 and nums[mid] <= nums[mid - 1]:
                high = mid - 1
            elif mid + 1 < n and nums[mid] <= nums[mid + 1]:
                low = mid + 1
            return mid
        return mid
        """
        n = len(nums)
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) / 2
            if mid != 0 and nums[mid - 1] > nums[mid]:
                high = mid - 1
            elif mid != n - 1 and nums[mid + 1] > nums[mid]:
                low = mid  + 1
            else:
                return mid
        return mid

