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
        def helper(cur):
            if not cur:
                return [0, 0]
            left_yes, left_no = helper(cur.left)
            right_yes, right_no = helper(cur.right)
            result = [0, 0]
            result[0] = left_no + right_no + cur.val
            result[1] = max(left_yes, left_no) + max(right_yes, right_no)
            return result
        result = helper(root)
        return max(result[0], result[1])