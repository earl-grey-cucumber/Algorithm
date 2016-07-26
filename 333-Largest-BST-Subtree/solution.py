# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        temp = [0,0, 0]
        self.helper(root, temp)
        return temp[2]
    
    def helper(self, cur, temp):
        if not cur:
            temp[0] = float("inf")
            temp[1] = float("-inf")
            temp[2] = 0

            return True
        lt = [0,0, 0]
        left = self.helper(cur.left, lt)
        rt = [0,0, 0]
        right = self.helper(cur.right, rt)
        if left and right and lt[1] <= cur.val <= rt[0]:
            temp[0] = min(cur.val, lt[0])
            temp[1] = max(cur.val, rt[1])
            temp[2] = lt[2] + rt[2] + 1
            return True
        else:
            temp[2] = max(lt[2], rt[2])
            return False
            
       
