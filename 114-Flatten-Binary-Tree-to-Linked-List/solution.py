# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        if not root:
            return
        stack = [root]
        while stack:
            cur = stack.pop(-1)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            cur.left = None
            if stack:
                cur.right = stack[-1]
    