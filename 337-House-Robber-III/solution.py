# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        result = [0]
        self.helper(root, result)
        return result[0]

    def helper(self, root, result):
        if not root:
            return (0, 0)
        left_yes, left_no = self.helper(root.left, result)
        right_yes, right_no = self.helper(root.right, result)
        result[0] = max(left_no + right_no + root.val, left_yes + right_yes)
        return result[0], left_yes + right_yes
