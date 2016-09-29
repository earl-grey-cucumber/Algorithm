class NumArray(object):
    def __init__(self, nums):
        def build_tree(nums):
            i, j = self.n, 0
            while i < 2 * self.n:
                self.tree[i] = nums[j]
                i += 1
                j += 1
            for k in range(self.n - 1, -1, -1):
                self.tree[k] = self.tree[k * 2] + self.tree[k * 2 + 1]
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        build_tree(nums)
       
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while (i > 0):
            left, right = i, i
            if i % 2 == 0:
                right = i + 1
            else:
                left = i - 1
            self.tree[i / 2] = self.tree[left] + self.tree[right]
            i /= 2

    def sumRange(self, i, j):
        i += self.n
        j += self.n
        sum = 0
        while i <= j:
            if i % 2 == 1:
                sum += self.tree[i]
                i += 1
            if j % 2 == 0:
                sum += self.tree[j]
                j -= 1
            i /= 2
            j /= 2
        return sum

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)