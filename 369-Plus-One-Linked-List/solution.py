# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        def add(head):
            if not head:
                return 1
            head.val += add(head.next)
            carry, head.val = divmod(head.val, 10)
            return carry
            
        carry = add(head)
        if carry and head:
            addc = ListNode(1)
            addc.next = head
            head = addc
        return head
