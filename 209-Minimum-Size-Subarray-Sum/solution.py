class Solution(object):
    def minSubArrayLen(self, s, nums):
        def helper(sums, i, target):
            low, high = i, len(sums) - 1
            index = len(sums) + 1
            while low <= high:
                mid = low + (high - low) / 2
                if sums[mid] >= target:
                    high = mid  -1
                    index = min(index, mid)
                else:
                    low = mid + 1
            return index
            
        n = len(nums)
        sums = [0] * (n + 1)
        for i in range(n):
            sums[i + 1] = sums[i] + nums[i]
        cand = n + 1
        for i in range(n + 1):
            index = helper(sums, i, sums[i] + s)
            if index <= n:
                cand = min(cand, index - i)
        if cand == n + 1:
            cand = 0
        return cand
        
        """
        n = len(nums)
        sums, start, min_len, i = 0, 0, n + 1, 0
        while i < n:
            sums += nums[i]
            while sums >= s:
                min_len = min(min_len, i - start + 1)
                sums -= nums[start]
                start += 1
            i += 1
        return min_len if min_len != n + 1 else 0
        """
        
        