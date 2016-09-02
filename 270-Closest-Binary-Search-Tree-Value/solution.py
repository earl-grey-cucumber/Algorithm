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
        result = root.val
        diff = abs(root.val - target)
        cur = root
        while cur:
            if cur.val == target:
                return cur.val
            if abs(cur.val - target) < diff:
                diff = abs(target - cur.val)
                result = cur.val
            if cur.val < target:
                cur = cur.right
            else:
                cur = cur.left
        return result