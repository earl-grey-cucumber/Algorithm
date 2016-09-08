# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        def helper(cur, p):
            if not cur:
                return p
            newRoot = helper(cur.left, cur)
            cur.left = p.right if p else None
            cur.right = p
            return newRoot
        if not root or not root.left:
            return root
        return helper(root, None)
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
        """