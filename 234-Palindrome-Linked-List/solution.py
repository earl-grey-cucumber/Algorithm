# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or not head.next:
            return True
        slow, fast = head, head.next # want to find last node of 1st half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        pre, cur = None, slow.next
        slow.next = None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            
        p, q = head, pre
        while q: 
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return True
