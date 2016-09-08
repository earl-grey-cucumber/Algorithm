# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        cur, p, left, right = root, None, None, None
        while cur:
            left = cur.left
            cur.left = right
            right = cur.right
            cur.right = p
            p = cur
            cur = left
        return p