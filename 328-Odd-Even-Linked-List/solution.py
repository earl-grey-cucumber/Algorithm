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
        head2 = head.next
        cur, tail = head, None
        while cur:
            if not cur.next:
                tail = cur
                break
            post = cur.next
            cur.next = post.next
            if post.next:
                post.next = post.next.next
            if not cur.next:
                tail = cur
                break
            cur = cur.next
        tail.next = head2
        return head
