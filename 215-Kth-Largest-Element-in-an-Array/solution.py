class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        return self.helper(nums, 0, n - 1, n - k + 1)
    
    def helper(self, nums, l, h, k):
        #if l == h:
        #   return nums[l]
        pos = random.randrange(0, h - l + 1, 1) + l
        temp = nums[pos]
        nums[pos] = nums[h]
        nums[h] = temp
        index = self.find(nums, l, h)
        if index - l + 1 == k:
            return nums[index]
        if index - l + 1 > k:
            return self.helper(nums, l, index - 1, k)
        return self.helper(nums, index + 1, h, k - (index - l + 1))
        
    def find(self, nums, l, h):
        i, j = l, l
        while j < h:
            if nums[j] < nums[h]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
            j += 1
        temp = nums[h]
        nums[h] = nums[i]
        nums[i] = temp
        return i