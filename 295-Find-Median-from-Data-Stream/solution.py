from heapq import *
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.heap1, self.heap2 = [], []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.heap2, num)
        heapq.heappush(self.heap1, -heapq.heappop(self.heap2))
        if len(self.heap1) > len(self.heap2) + 1:
            heapq.heappush(self.heap2, -heapq.heappop(self.heap1))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if not self.heap1:
            return 0.0
        if not self.heap2:
            return -self.heap1[0] * 1.0
        if (len(self.heap2) + len(self.heap1)) % 2 == 1:
            return -self.heap1[0] * 1.0
        else:
            return -self.heap1[0] * 0.5 + self.heap2[0] * 0.5
            
# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()