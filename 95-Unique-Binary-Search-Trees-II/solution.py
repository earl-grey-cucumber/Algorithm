# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.helper(0, n - 1)
    
    def helper(self, low, high):
        if high < low:
            return [None]
        result = []
        for i in range(low, high + 1):
            left = self.helper(low, i - 1)
            right = self.helper(i + 1, high)
            for j in range(len(left)):
                for k in range(len(right)):
                    root = TreeNode(i + 1)
                    root.left = left[j]
                    root.right = right[k]
                    result.append(root)
        return result