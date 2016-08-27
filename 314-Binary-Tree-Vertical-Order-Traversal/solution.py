# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        left, right = 0, 0
        result, maps = [], {}
        queue = [[root, 0]]
        while queue:
            size = len(queue)
            for i in range(size):
                cur, col = queue.pop(0)
                if col not in maps:
                    maps[col] = []
                maps[col].append(cur.val)
                left, right = min(left, col), max(right, col)
                if cur.left:
                    queue.append([cur.left, col - 1])
                if cur.right:
                    queue.append([cur.right, col + 1])
        i = left
        while i <= right:
            result.append(maps[i])
            i += 1
        return result
            