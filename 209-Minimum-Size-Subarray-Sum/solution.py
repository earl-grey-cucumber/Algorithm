class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        def helper(low, sums, target):
            high, cand = len(sums) - 1, len(sums)
            while low <= high:
                mid = (low + high) / 2
                if sums[mid] >= target:
                    cand = min(cand, mid)
                    high = mid - 1
                else:
                    low = mid + 1
            return cand
        min_len = sys.maxint
        n = len(nums)
        sums = [0 for i in range(n + 1)]
        for i in range(n):
            sums[i + 1] = sums[i] + nums[i]
        for i in range(n + 1):
            index = helper(i, sums, s + sums[i])
            if i < index <= n:
                min_len = min(min_len, index - i)
        return min_len if min_len != sys.maxint else 0
        
            