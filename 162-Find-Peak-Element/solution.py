class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        low, high = 0, n - 1
        while low <= high:
            mid = (high + low) / 2
            if mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                high = mid - 1
            elif mid + 1 < n and nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                return mid
        return mid
        

