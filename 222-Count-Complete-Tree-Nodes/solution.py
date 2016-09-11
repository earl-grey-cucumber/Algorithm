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
        def helper(root):
            if not root:
                return 0
            l, r = helper1(root.left), helper2(root.right)
            if l == r:
                return (1 << (l + 1)) - 1
            else:
                return 1 + helper(root.left) + helper(root.right)
        def helper1(cur):
            if not cur:
                return 0
            return 1 + helper1(cur.left)
        def helper2(cur):
            if not cur:
                return 0
            return 1 + helper2(cur.right)
        
        return helper(root)
   
        