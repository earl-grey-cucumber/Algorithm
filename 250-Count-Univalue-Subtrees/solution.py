# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(cur):
            if not cur:
                return True
            left = helper(cur.left)
            right = helper(cur.right)
            if not left or not right:
                return False
            if cur.left and cur.left.val != cur.val:
                return False
            if cur.right and cur.right.val != cur.val:
                return False
            result[0] += 1
            return True
        result = [0]
        helper(root)
        return result[0]