# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        def dfs(cur, result, path):
            if not cur.left and not cur.right:
                result.append(path + str(cur.val))
                return
            if cur.left:
                dfs(cur.left, result, path + str(cur.val) + "->")
            if cur.right:
                dfs(cur.right, result, path + str(cur.val) + "->")

        result = []
        dfs(root, result, "")
        return result