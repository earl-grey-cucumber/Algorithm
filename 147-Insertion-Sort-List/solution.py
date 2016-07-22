# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        pre, cur = dummy, head
        dummy.next = head
        while cur.next:
            if cur.val > cur.next.val:
                while pre.next and pre.next.val < cur.next.val:
                    pre = pre.next
                node = cur.next
                cur.next = node.next
                node.next = pre.next
                pre.next = node
                pre = dummy
            else:
                cur = cur.next
        return dummy.next
