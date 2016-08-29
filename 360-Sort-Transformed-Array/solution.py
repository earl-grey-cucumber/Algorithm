class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def func(num, a, b, c):
            return a * num * num + b * num + c
        result = []
        n = len(nums)
        if a >= 0:
            low, high = 0, n - 1
            while low <= high:
                val1, val2 = func(nums[low], a, b, c), func(nums[high], a, b, c)
                if val1 > val2:
                    result.append(val1)
                    low += 1
                else:
                    result.append(val2)
                    high -= 1
            result = result[::-1]
        else:
            low, high = 0, n - 1
            while low <= high:
                val1, val2 = func(nums[low], a, b, c), func(nums[high], a, b, c)
                if val1 < val2:
                    result.append(val1)
                    low += 1
                else:
                    result.append(val2)
                    high -= 1
        return result
        