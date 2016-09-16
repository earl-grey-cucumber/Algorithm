class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        i, l, known_sum, count = 0, len(nums), 1, 0
        while known_sum <= n:
            if i < l and nums[i] <= known_sum:
                known_sum += nums[i]
                i += 1
            else:
                count += 1
                known_sum *= 2
        return count