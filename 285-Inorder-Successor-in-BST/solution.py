# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        cur, suc = root, None
        while cur:
            if cur.val > p.val:
                suc = cur
                cur = cur.left
            else:
                cur = cur.right
        return suc