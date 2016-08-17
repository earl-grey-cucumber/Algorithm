class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        dp = [0 for i in range(target + 1)]
        dp[0] = 1
        for i in range(target + 1):
            for j in range(len(nums)):
                if i + nums[j] <= target:
                    dp[i + nums[j]] += dp[i]
        return dp[target]