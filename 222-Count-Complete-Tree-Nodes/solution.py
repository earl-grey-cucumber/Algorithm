# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.depth_left(root.left)
        right = self.depth_right(root.right)
        if left == right:
            return (1 << (left + 1)) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
    def depth_left(self, cur):
        if not cur:
            return 0
        return 1 + self.depth_left(cur.left)
        
    def depth_right(self, cur):
        if not cur:
            return 0
        return 1 + self.depth_right(cur.right)