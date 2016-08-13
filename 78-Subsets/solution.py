class Solution(object):
    def subsets(self, nums):
        result = []
        n = len(nums)
        for i in range(1 << n):
            path = []
            for j in range(n):
                if (i >> j) & 1:
                    path.append(nums[j])
            result.append(path)
        return result