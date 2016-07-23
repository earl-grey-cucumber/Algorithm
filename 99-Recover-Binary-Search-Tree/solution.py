# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    p, q, pre = None, None, None
    def recoverTree(self, root):
        global p, q, pre
        p, q, pre = None, None, None
        if not root:
            return
        self.helper(root)
        temp = p.val
        p.val = q.val
        q.val = temp
    
    def helper(self, cur):
        global p, q, pre
        if not cur:
            return
        self.helper(cur.left)
        if pre and pre.val > cur.val:
            if not p:
                p = pre
                q = cur
            else:
                q = cur
        pre = cur
        self.helper(cur.right)