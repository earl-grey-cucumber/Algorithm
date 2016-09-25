# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        queue = [root]
        sum = 0
        while queue:
            cur = queue.pop(0)
            if cur.left and not cur.left.left and not cur.left.right:
                sum += cur.left.val
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return sum
            