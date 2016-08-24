class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def rotate_helper(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        size = len(nums)
        k = k % size
        rotate_helper(nums, 0, size - 1)
        rotate_helper(nums, 0, k - 1)
        rotate_helper(nums, k, size - 1)
