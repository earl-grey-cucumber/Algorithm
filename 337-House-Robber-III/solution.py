# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [0]
        def helper(cur, result):
            if not cur:
                return [0, 0]
            left_yes, left_no = helper(cur.left, result)
            right_yes, right_no = helper(cur.right, result)
            result[0] = max(left_yes + right_yes, left_no + right_no + cur.val)
            return result[0], left_yes + right_yes
        helper(root, result)
        return result[0]