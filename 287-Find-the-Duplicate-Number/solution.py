class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n, max_val = len(nums), nums[0]
        for num in nums:
            max_val = max(max_val, num)
        low, high = 1, max_val
        while low <= high:
            if low == high:
                return low
            mid = low + (high - low) / 2
            count = 0
            for num in nums:
                if low <= num <= mid:
                    count += 1
            if count > mid - low + 1:
                high = mid
            else:
                low = mid + 1
        return -1