import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        if k <= 0:
            return []
        dic = {}
        result = []
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        heap = []
        for i in dic:
            #print(str(dic[i]) + " " + str(i))
            #print(len(heap))
            if len(heap) < k:
                heap.append([dic[i], i])
                if len(heap) == k:
                    heapq.heapify(heap)
            elif heapq.nsmallest(1, heap)[0][0] < dic[i]:
                #print(heapq.nsmallest(1, heap)[0][0])
                heapq.heappop(heap)
                heapq.heappush(heap, [dic[i], i])
        while k > 0:
            cur = heapq.heappop(heap)
            result.append(cur[1])
            k -= 1
        return result