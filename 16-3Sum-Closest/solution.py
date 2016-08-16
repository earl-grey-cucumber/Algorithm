class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        i, n, result = 0, len(nums), sys.maxint
        while i < n:
            j, k = i + 1, n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if abs(sum - target) < abs(result - target): #closest may < 0
                    result = sum
                if sum == target:
                    return target
                elif sum < target:
                    j += 1
                else:
                    k -= 1
            i += 1
        return result