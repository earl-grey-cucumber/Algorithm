from collections import defaultdict
from heapq import *
class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return str
        maps = defaultdict(int)
        for s in str:
            maps[s] += 1
        heap = []
        for key, val in maps.iteritems():
            heap.append([-val, key])
        heapify(heap)
        result = []
        while heap:
            used = []
            i = 0
            pre_len = len(result)
            while i < min(k, len(str) - pre_len):
                if not heap:
                    return ""
                cur = heappop(heap)
                result.append(cur[1])
                cur[0] += 1
                if cur[0] < 0:
                    used.append(cur)
                i += 1
            for item in used:
                heappush(heap, item)
        return "".join(result)

