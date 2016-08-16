class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                break
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        return i + 1, j + 1