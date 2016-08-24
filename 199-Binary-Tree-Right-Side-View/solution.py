# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(cur, result, depth):
            if not cur:
                return
            if depth >= len(result):
                result.append(cur.val)
            dfs(cur.right, result, depth + 1)
            dfs(cur.left, result, depth + 1)
        result = []
        dfs(root, result, 0)
        return result