class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        n = len(nums)
        dp = []
        for i in range(n):
            l, h = 0, len(dp) - 1
            while l <= h:
                mid = l + (h - l) / 2
                if dp[mid] < nums[i]:
                    low = mid + 1
                else:
                    high = mid - 1
            if l < len(dp):
                dp[l] = num[i]
            else:
                dp.append(nums[i])
        
        """
        size = len(nums)
        dp = []
        for x in range(size):
            low, high = 0, len(dp) - 1
            while low <= high:
                mid = (low + high) / 2
                if dp[mid] < nums[x]:
                    low = mid + 1
                else:
                    high = mid - 1
            if low < len(dp):
                dp[low] = nums[x]
            else:
                dp.append(nums[x])
        return len(dp)
