class Solution(object):
    def lengthOfLIS(self, nums):
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


