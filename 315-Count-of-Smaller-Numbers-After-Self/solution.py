class Treenode(object):
    def __init__(self, x):
        self.val = x
        self.left, self.right = None, None
        self.cnt, self.leftcnt = 1, 0
        
class BST(object):
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        if not self.root:
            self.root = Treenode(val)
            return 0
        cnt = 0
        cur = self.root
        while cur:
            if val < cur.val:
                cur.leftcnt += 1
                if not cur.left:
                    cur.left = Treenode(val)
                    break
                cur = cur.left
            elif val > cur.val:
                cnt += cur.leftcnt + cur.cnt
                if cur.right is None:
                    cur.right = Treenode(val)
                    break
                cur = cur.right
            else:
                cnt += cur.leftcnt
                cur.cnt += 1
                break
        return cnt

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        bst = BST()
        for i in range(n - 1, -1, -1):
            result[i] = bst.insert(nums[i])
        return result