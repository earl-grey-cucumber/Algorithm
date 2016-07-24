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
        if not root or not root.left:
            return root
        return self.helper(root, None)
        
    def helper(self, cur, par):
        if not cur:
            return par
        new_root = self.helper(cur.left, cur)
        cur.left = par.right if par else None
        cur.right = par
        return new_root
    
    """
    pre, cur, left, right = None, root, None, None
        while cur:
            left = cur.left
            cur.left = right
            right = cur.right
            cur.right = pre
            pre = cur
            cur = left
        return pre

    """