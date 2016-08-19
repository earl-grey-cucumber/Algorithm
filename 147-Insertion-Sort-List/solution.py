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
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        while cur.next:
            post = cur.next.next
            if cur.val > cur.next.val:
                pre = dummy
                while pre.next and pre.next.val < cur.next.val:
                    pre = pre.next
                temp = cur.next
                cur.next = post
                temp.next = pre.next
                pre.next = temp
                #cur = post
            else:
                cur = cur.next
            if not cur:
                break
        return dummy.next