from random import randint
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        
    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        result = None
        count = 0
        for i, num in enumerate(self.nums):
            if num != target:
                continue
            index = randint(0, count)
            count += 1
            if index == 0:
                result = i
        return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)