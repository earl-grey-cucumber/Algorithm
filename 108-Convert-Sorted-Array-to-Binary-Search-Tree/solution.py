# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(nums, low, high):
            if low > high:
                return None
            mid = low + (high - low) / 2
            cur = TreeNode(nums[mid])
            cur.left = helper(nums, low, mid - 1)
            cur.right = helper(nums, mid + 1, high)
            return cur
            
        return helper(nums, 0, len(nums) - 1)