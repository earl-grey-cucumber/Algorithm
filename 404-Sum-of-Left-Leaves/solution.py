# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        sum = [0]
        def helper(cur, is_left, sum):
            if not cur:
                return 0
            if is_left and not cur.left and not cur.right:
                sum[0] += cur.val
            helper(cur.left, True, sum)
            helper(cur.right, False, sum)
        helper(root.left, True, sum)
        helper(root.right, False, sum)
        return sum[0]