# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        def countNodes(cur):
            if not cur:
                return 0
            return 1 + countNodes(cur.left) + countNodes(cur.right)
        count = countNodes(root.left)
        if k <= count:
            return self.kthSmallest(root.left, k)
        elif k > count + 1:
            return self.kthSmallest(root.right, k-1-count)
        return root.val

        """
        cur, stack = root, []
        while k > 0 and (cur or stack):
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                k -= 1
                if k == 0:
                    return cur.val
                cur = cur.right
        return cur
        """