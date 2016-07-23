# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        result = []
        self.dfs(root, sum, result, [])
        return result
    
    def dfs(self, cur, sum, result, path):
        if not cur:
            return result
        #path.append(cur.val)
        if not cur.left and not cur.right:
            if sum == cur.val:
                result.append(path[:] + [cur.val])
            return
        self.dfs(cur.left, sum - cur.val, result, path + [cur.val])
        self.dfs(cur.right, sum - cur.val, result, path + [cur.val])
        
        