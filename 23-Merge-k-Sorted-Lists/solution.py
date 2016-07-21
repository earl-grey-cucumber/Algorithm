# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        heap = []
        for l in lists:
            if l:
                heap.append([l.val, l])
        heapq.heapify(heap)
        head = ListNode(0)
        pre = head
        while heap:
            cur = heapq.heappop(heap)[1]
            pre.next = cur
            pre = cur
            if cur.next:
                heapq.heappush(heap, [cur.next.val, cur.next])
        return head.next
        