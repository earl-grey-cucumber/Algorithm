# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        if not root:
            return []
        left, right, result = [], [], []
        self.helper1(root, target, left)
        self.helper2(root, target, right)
        while k > 0:
            if not left:
                result.append(right.pop())
            elif not right:
                result.append(left.pop())
            elif target - left[-1] < right[-1] - target:
                result.append(left.pop())
            else:
                result.append(right.pop())
            k -= 1
        return result
    
    def helper1(self, cur, target, left):
        if not cur:
            return
        self.helper1(cur.left, target, left)
        if cur.val > target:
            return
        left.append(cur.val)
        self.helper1(cur.right, target, left)
        
    def helper2(self, cur, target, right):
        if not cur:
            return
        self.helper2(cur.right, target, right)
        if cur.val <= target:
            return
        right.append(cur.val)
        self.helper2(cur.left, target, right)
                