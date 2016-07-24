# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 0)
        
    def helper(self, cur, sums):
        if not cur:
            return 0
        sums = sums * 10 + cur.val
        if not cur.left and not cur.right:
            return sums
        return self.helper(cur.left, sums) + self.helper(cur.right, sums)