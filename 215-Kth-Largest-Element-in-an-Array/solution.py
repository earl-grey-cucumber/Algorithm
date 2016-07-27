class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n < k:
            return -1
        heap = []
        for i in range(n):
            if len(heap) < k:
                heap.append([nums[i], i])
                if len(heap) == k:
                    heapq.heapify(heap)
            elif heapq.nsmallest(1, heap)[0][0] < nums[i]:
                heapq.heappop(heap)
                heapq.heappush(heap, [nums[i], i])
        return heapq.heappop(heap)[0]
                
