class NumArray(object):
    def __init__(self, nums):
        self.sums = [0] * (len(nums) + 1)
        for i in xrange(1, len(nums) + 1):
            self.sums[i] = self.sums[i - 1] + nums[i - 1]

    def sumRange(self, i, j):
        return self.sums[j + 1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)