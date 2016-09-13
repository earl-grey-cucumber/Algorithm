class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        queue, result = [], []
        for i in range(k):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop(-1)
            queue.append(i)
        for i in range(k, len(nums)):
            result.append(nums[queue[0]])
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop(-1)
            while queue and queue[0] + k <= i:
                queue.pop(0)
            queue.append(i)
        result.append(nums[queue[0]])
        return result
