class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, n = 1, len(nums)
        flag = False
        while i < n:
            if not flag and nums[i - 1] > nums[i]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            if flag and nums[i - 1] < nums[i]:
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
            i += 1
            flag = not flag
        