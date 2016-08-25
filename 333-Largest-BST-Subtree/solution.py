# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        #temp = [float("inf"),float("-inf"), 0]
        return self.helper(root)[2]
        #return temp[2]
        
    def helper(self, root):
        if not root:
            return [float("inf"), float("-inf"), 0, True]
        #left_temp = [float("inf"),float("-inf"), 0]
        left0, left1, left2, left3 = self.helper(root.left)
        #right_temp = [float("inf"),float("-inf"), 0]
        right0, right1, right2, right3 = self.helper(root.right)
        is_bst = False
        if left3 and right3 and left1 <= root.val and root.val <= right0:
            return [
                min(root.val, left0),
                max(root.val, right1),
                left2 + right2 + 1,
                True]
        else:
            return [float("inf"), float("-inf"), max(left2, right2), False]
