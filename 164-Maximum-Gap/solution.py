class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def counting_sort(nums, base, n):
            count = [0] * 10
            output = [0] * n
            for i in range(n):
                count[(nums[i] / base) % 10] += 1
            for i in range(1, 10):
                count[i] += count[i - 1]
            for i in range(n - 1, -1, -1):
                output[count[(nums[i] / base) % 10] - 1] = nums[i]
                count[(nums[i] / base) % 10] -= 1
            for i in range(n):
                nums[i] = output[i]
        if len(nums) < 2:
            return 0
        max_val = nums[0]
        for num in nums:
            max_val = max(max_val, num)
        base,n = 1, len(nums)
        while max_val > 0:
            counting_sort(nums, base, n)
            base *= 10
            max_val /= 10
        max_gap = float("-inf")
        for i in range(1, n):
            max_gap = max(max_gap, nums[i] - nums[i - 1])
        return max_gap