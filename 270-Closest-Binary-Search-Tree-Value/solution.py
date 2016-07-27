# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return -1
        cur = root
        min_diff = abs(root.val - target)
        candidate = root.val
        while cur:
            diff = abs(cur.val - target)
            if diff == 0:
                return cur.val
            if diff < min_diff:
                candidate = cur.val
                min_diff = diff
            if cur.val > target:
                cur = cur.left
            else:
                cur = cur.right
        return candidate
            