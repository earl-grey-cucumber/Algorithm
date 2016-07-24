# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.cur = root
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur or self.stack

    def next(self):
        """
        :rtype: int
        """
        self.cur = self.stack.pop()
        nextVal = self.cur.val
        self.cur = self.cur.right
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        return nextVal

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())