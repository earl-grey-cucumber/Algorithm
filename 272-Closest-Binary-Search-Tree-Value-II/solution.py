# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        def helper1(cur, target, s1):
            if not cur:
                return
            helper1(cur.left, target, s1)
            if cur.val > target:
                return
            s1.append(cur.val)
            helper1(cur.right, target, s1)
        def helper2(cur, target, s2):
            if not cur:
                return
            helper2(cur.right, target, s2)
            if cur.val <= target:
                return
            s2.append(cur.val)
            helper2(cur.left, target, s2)
        stack1, stack2 = [], []
        helper1(root, target, stack1)
        helper2(root, target, stack2)
        i, j, l = 0, len(stack1) - 1, len(stack2) - 1
        result = []
        while i < k:
            if j < 0:
                result.append(stack2[l])
                l -= 1
            elif l < 0:
                result.append(stack1[j])
                j -= 1
            elif target - stack1[j] <= stack2[l] - target:
                result.append(stack1[j])
                j -= 1
            else:
                result.append(stack2[l])
                l -= 1
            i += 1
        return result
                