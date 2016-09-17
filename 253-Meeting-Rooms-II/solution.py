# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1
        heap, count = [], 0 # or count = 1 no need for “if len(n)==1: return 1:
        heapq.heapify(heap)  
        intervals.sort(lambda a, b : a.start - b.start)  
        heapq.heappush(heap, (intervals[0].end, intervals[0]))
        for i in range(1, len(intervals)):
            cur = intervals[i]
            while heap and cur.start >= heapq.nsmallest(1, heap, key=lambda s: s[0])[0][0]:
                heapq.heappop(heap)
            heapq.heappush(heap, (cur.end, cur))
            count = max(count, len(heap))
        return count
