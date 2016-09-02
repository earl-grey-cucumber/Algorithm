class Solution(object):
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        dp = [nums[0]]
        if n == 1:
            return dp[0]
            
        dp.append(max(nums[0], nums[1]))
        if n == 2:
            return dp[1]   
            
        dp.append(0)   
        for i in range(2, n - 1):
            dp[2] = max(dp[0] + nums[i], dp[1])
            dp[0] = dp[1]
            dp[1] = dp[2]
        cand1 = dp[1]
        
        dp2 = [0, nums[1]]
        dp2.append(0)
        for i in range(2, n):
            dp2[2] = max(dp2[0] + nums[i], dp2[1])
            dp2[0] = dp2[1]
            dp2[1] = dp2[2]
        cand2 = dp2[1]
        return max(cand1, cand2)
