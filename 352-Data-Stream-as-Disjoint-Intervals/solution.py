# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []
        
    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        def get_up(nums, val):
            low, high, up = 0, len(nums) - 1, len(nums)
            while low <= high:
                mid = low + (high - low) / 2
                if nums[mid].start >= val:
                    up = min(up, mid)
                    high = mid - 1
                else:
                    low = mid + 1
            return up
            
        up = get_up(self.intervals, val)
        news, newe = val, val
        if up > 0 and self.intervals[up - 1].end  + 1 >= val:
            up -= 1
        while up < len(self.intervals) and val + 1 >= self.intervals[up].start:
            news = min(news, self.intervals[up].start)
            newe = max(newe, self.intervals[up].end)
            del self.intervals[up]
        self.intervals.insert(up, Interval(news, newe))

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()