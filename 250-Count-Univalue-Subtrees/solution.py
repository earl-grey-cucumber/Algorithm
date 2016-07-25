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
        count = [0]
        self.helper(root, count)
        return count[0]
        
    def helper(self, cur, count):
        if not cur:
            return True

        left = self.helper(cur.left, count)
        right = self.helper(cur.right, count)
        if not left or not right:
            return False
        if cur.left and cur.left.val != cur.val:
            return False
        if cur.right and cur.right.val != cur.val:
            return False
        count[0] += 1
        return True