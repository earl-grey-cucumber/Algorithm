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
        result = []
        q = [["", root]]
        while q:
            size = len(q)
            for i in range(size):
                path, cur = q.pop(0)
                if not cur.left and not cur.right:
                    result.append(path + str(cur.val))
                else:
                    if cur.left:
                        q.append([path + str(cur.val) + "->", cur.left])
                    if cur.right:
                        q.append([path + str(cur.val) + "->", cur.right])
        return result