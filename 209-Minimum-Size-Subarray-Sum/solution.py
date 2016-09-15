class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 0
        cur_sum = 0
        min_len = sys.maxint
        while j < len(nums):
            cur_sum += nums[j]
            while cur_sum >= s:
                min_len = min(min_len, j - i + 1)
                cur_sum -= nums[i]
                i += 1
            j += 1
        return min_len if min_len != sys.maxint else 0
            