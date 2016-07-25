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
        if p.right:
            cur = p.right
            while cur and cur.left:
                cur = cur.left
            return cur
        else:
            suc, cur = None, root
            while cur:
                if cur.val > p.val:
                    suc = cur
                    cur = cur.left
                elif cur.val < p.val:
                    cur = cur.right
                else:
                    break
            return suc