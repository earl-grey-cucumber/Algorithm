# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(cur):
            if not cur:
                return 0
            len = 1
            left = helper(cur.left)
            right = helper(cur.right)
            if cur.left and cur.val + 1 == cur.left.val:
                len = left + 1
            if cur.right and cur.val + 1 == cur.right.val:
                len = max(len, right + 1)
            result[0] = max(len, result[0])
            return len
        result = [0]
        helper(root)
        return result[0]