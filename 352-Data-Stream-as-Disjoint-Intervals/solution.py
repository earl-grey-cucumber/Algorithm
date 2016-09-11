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
        def upper_bound(nums, target):
            left, right = 0, len(nums) - 1
            cand = len(nums)
            while left <= right:
                mid = left + (right - left) / 2
                if nums[mid].start > target:
                    right = mid - 1
                    cand = min(cand, mid)
                else:
                    left = mid + 1
            return cand

        i = upper_bound(self.intervals, val)
        start, end = val, val
        if i != 0 and self.intervals[i-1].end + 1 >= val:
            i -= 1
        while i != len(self.intervals) and \
              end + 1 >= self.intervals[i].start:
            start = min(start, self.intervals[i].start)
            end = max(end, self.intervals[i].end);
            del self.intervals[i]
        self.intervals.insert(i, Interval(start, end))
        
    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()