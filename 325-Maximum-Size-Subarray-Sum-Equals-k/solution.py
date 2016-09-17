class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n, max_len, cur_sum = len(nums), 0, 0
        maps = {0: -1}
        for i in range(n):
            cur_sum += nums[i]
            if cur_sum - k in maps:
                max_len = max(max_len, i - maps[cur_sum - k])
            if cur_sum not in maps:
                maps[cur_sum] = i
        return max_len
            