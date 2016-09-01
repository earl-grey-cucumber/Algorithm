class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        nums = [0] * (length + 1)
        for update in updates:
            s, e, change = update[0], update[1], update[2]
            nums[s] += change
            nums[e + 1] -= change
        sum = 0
        for i in range(len(nums) - 1):
            sum += nums[i]
            nums[i] = sum
        return nums[:-1]