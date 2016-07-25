# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = [[]]
        self.dfs(root, result)
        return result
    
    def dfs(self, cur, result):
        if not cur:
            return -1
        if not cur.left and not cur.right:
            result[0].append(cur.val)
            return 0
        d1 = self.dfs(cur.left, result)
        d2 = self.dfs(cur.right, result)
        d = max(d1, d2) + 1
        if len(result) == d:
            result.append([])
        result[d].append(cur.val)
        return d
        