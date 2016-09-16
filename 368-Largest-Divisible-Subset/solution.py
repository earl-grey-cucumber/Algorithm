class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        result = []
        n = len(nums)
        dp = [[] for i in range(n)]
        nums = sorted(nums)
        dp[0] = [nums[0]]
        for i in range(n):
            dp[i] = []
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[i]) < len(dp[j]):
                        dp[i] = dp[j][:]
            dp[i].append(nums[i])
            if len(dp[i]) > len(result):
                result = dp[i]
        return result