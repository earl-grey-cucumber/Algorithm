class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(nums, [], result, 0)
        return result
    
    def dfs(self, nums, path, result, index):
        result.append(path)
        if index == len(nums):
            return
        for i in range(index, len(nums)):
            self.dfs(nums, path + [nums[i]], result, i + 1)