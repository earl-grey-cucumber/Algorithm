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
        result = []
        if not root:
            return result
        self.helper(root, result, "")
        return result
    
    def helper(self, root, result, path):
        if not root.left and not root.right:
            result.append(path + str(root.val))
            return
        if root.left:
            self.helper(root.left, result, path  + str(root.val) + "->")
        if root.right:
            self.helper(root.right, result, path + str(root.val) + "->")