# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.helper(root, result, 0)
        return result[::-1]
    
    def helper(self, cur, result, depth):
        if not cur:
            return result
        if depth >= len(result):
            result.append([cur.val])
        else:
            result[depth].append(cur.val)
        self.helper(cur.left, result, depth + 1)
        self.helper(cur.right, result, depth + 1)