import math
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        max_gap = float("-inf")
        max_val, min_val = nums[0], nums[0]
        for num in nums:
            max_val = max(max_val, num)
            min_val = min(min_val, num)
        gap = int(math.ceil(float(max_val - min_val) / (n - 1)))
        start = [max_val + 1] * (n - 1)
        end = [min_val - 1] * (n - 1)
        for i in range(n):
            if nums[i] == max_val or nums[i] == min_val:
                continue
            id = (nums[i] - min_val) / gap
            start[id] = min(start[id], nums[i])
            end[id] = max(end[id], nums[i])
        pre = min_val
        for i in range(n - 1):
            if start[i] == max_val + 1:
                continue
            max_gap = max(max_gap, start[i] - pre)
            pre = end[i]
        max_gap = max(max_gap, max_val - pre)
        return max_gap