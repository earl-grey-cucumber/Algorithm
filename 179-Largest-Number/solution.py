class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = sorted(nums, cmp=lambda x, y: cmp(str(y) + str(x), str(x) + str(y)))
        result = ""
        for num in nums:
            result += str(num)
        return result.lstrip("0") or "0"
            