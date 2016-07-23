# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.dfs(root, result)
        return result
    
    def dfs(self, cur, result):
        if not cur:
            return result
        self.dfs(cur.left, result)
        result.append(cur.val)
        self.dfs(cur.right, result)