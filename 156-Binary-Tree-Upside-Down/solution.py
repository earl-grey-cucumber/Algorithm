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
        parent, right, cur, post = None, None, root, None
        while cur:
            post = cur.left
            cur.left = right
            right = cur.right
            cur.right = parent
            parent = cur
            cur = post
        return parent