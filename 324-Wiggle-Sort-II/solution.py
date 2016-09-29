class Solution(object):
    def wiggleSort(self, nums):
        n = len(nums)
        if n <= 1:
            return
        copy = [0] * n
        for i in range(n):
            copy[i] = nums[i]
        if n % 2 == 1:
            mid_val = self.helper(copy, 0, n - 1, n / 2 + 1)
            answer = [mid_val] * n
            left, right = 0, n - 2
            for i in range(n):
                if nums[i] < mid_val:
                    answer[left] = nums[i]
                    left += 2
                elif nums[i] > mid_val:
                    answer[right] = nums[i]
                    right -= 2
        else:
            mid_val = self.helper(copy, 0, n - 1, n / 2)
            answer = [mid_val] * n
            left, right = n - 2, 1
            for i in range(n):
                if nums[i] < mid_val:
                    answer[left] = nums[i]
                    left -= 2
                elif nums[i] > mid_val:
                    answer[right] = nums[i]
                    right += 2
        for i in range(n):
            nums[i] = answer[i]
        
    def helper(self, nums, l, h, k):
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
