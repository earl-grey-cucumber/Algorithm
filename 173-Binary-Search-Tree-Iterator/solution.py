# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        self.stack = []
        self.cur = root
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left

    def hasNext(self):
        return self.cur or self.stack

    def next(self):
        self.cur = self.stack.pop()
        val = self.cur.val
        self.cur = self.cur.right
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        return val