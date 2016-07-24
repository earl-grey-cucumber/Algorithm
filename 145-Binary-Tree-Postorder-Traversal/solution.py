# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        stack, result = [], []
        cur, pre = root, None
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                peek = stack[-1]
                if peek.right and peek.right != pre:
                    cur = peek.right
                else:
                    result.append(peek.val)
                    stack.pop()
                    pre = peek
        return result
        
        """
        if not root:
            return []
        result, stack = [], [root]
        while stack:
            cur = stack.pop()
            result.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return result[::-1]
        """