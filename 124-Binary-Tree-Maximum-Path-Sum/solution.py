# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global max_path
        max_path = float("-inf")
        self.helper(root)
        return max_path
    
    def helper(self, cur):
        global max_path
        if not cur:
            return float("-inf")
        left = max(0, self.helper(cur.left))
        right = max(0, self.helper(cur.right))
        max_path = max(max_path, left + right + cur.val)
        return max(left + cur.val, right + cur.val)