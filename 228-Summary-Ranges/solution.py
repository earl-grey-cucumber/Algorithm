class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        result = []
        pre, i = 0, 1
        while i < len(nums) + 1:
            val = nums[i] if i < len(nums) else sys.maxint
            if nums[i - 1] + 1 == val:
                i += 1
                continue
            elif i - 1 == pre:
                result.append(str(nums[pre]))
            else:
                result.append(str(nums[pre]) + "->" + str(nums[i - 1]))
            pre = i
            i += 1
        return result
                
        