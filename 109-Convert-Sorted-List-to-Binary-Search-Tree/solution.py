# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    cur = None
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        global cur
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        cur = head
        return self.helper(0, count - 1)
    
    def helper(self, low, high):
        global cur
        if low > high:
            return None
        mid = low + (high - low) / 2
        left = self.helper(low, mid - 1)
        root = TreeNode(cur.val)
        cur = cur.next
        right = self.helper(mid + 1, high)
        root.left, root.right = left, right
        return root