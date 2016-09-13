class Solution(object):
    def verifyPreorder(self, preorder):
        stack = []
        low = float('-inf')
        for p in preorder:
            if p < low:
                return False
            while stack and p > stack[-1]:
                low = stack.pop()
            stack.append(p)
        return True
        """
        n = len(preorder)
        return self.helper(preorder, 0, n - 1)
    
    def helper(self, preorder, low, high):
        if low >= high:
            return True
        val = preorder[low]
        i = low + 1
        while i <= high and preorder[i] < val:
            i += 1
        j = i # j=i=start of right subtree
        while j <= high:
            if preorder[i] < val:
                return False
            j += 1
        left, right = True, True
        if i - 1 > low + 1:
            left = self.helper(preorder, low + 1, i - 1)
        if i < high:
            right = self.helper(preorder, i, high)
        return left and right
    stack = []
    low = float('-inf')
    for p in preorder:
        if p < low:
            return False
        while stack and p > stack[-1]:
            low = stack.pop()
        stack.append(p)
    return Truestack = []
    low = float('-inf')
    for p in preorder:
        if p < low:
            return False
        while stack and p > stack[-1]:
            low = stack.pop()
        stack.append(p)
    return True
        """
