class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap = []
        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                count += 1
                if count <= k:
                    heapq.heappush(heap, [-(nums1[i] + nums2[j]), nums1[i], nums2[j]])
                else:
                    top = -heap[0][0]
                    if nums1[i] + nums2[j] < top:
                        heapq.heappop(heap)
                        heapq.heappush(heap, [-(nums1[i] + nums2[j]), nums1[i], nums2[j]])
        result = []
        while heap:
            cur = heapq.heappop(heap)
            result.append([cur[1], cur[2]])
        return result[::-1]