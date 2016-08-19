# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        left, right = dummy, head
        while right.next:
            if right.val != 9:
                left = right
            right = right.next
        if right.val != 9:
            right.val += 1
            return dummy.next
        else:
            left.val += 1
            right = left.next
            while right:
                right.val = 0
                right = right.next
        return dummy.next if dummy.val == 0 else dummy