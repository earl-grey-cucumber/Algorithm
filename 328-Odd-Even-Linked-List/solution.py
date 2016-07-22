# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur1, head2, tail1 = head, head.next, None
        while cur1:
            if not cur1.next:
                tail1 = cur1
                break
            cur2 = cur1.next
            cur1.next = cur2.next
            if cur2.next:
                cur2.next = cur2.next.next
            if not cur1.next:
                tail1 = cur1
                break
            cur1 = cur1.next
        tail1.next = head2
        return head