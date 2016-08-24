# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, pre = head, None
        while cur:
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post
        return pre