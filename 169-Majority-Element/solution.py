class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask =    0xFFFFFFFF
        max_int = 0x7FFFFFFF

        n = 32
        bits = [0 for i in range(n)]
        for num in nums:
            for i in range(n):
                if (num >> i) & 1 == 1:
                    bits[i] += 1
        result = 0
        for i in range(n):
            if bits[i] * 2 > len(nums): 
                result += (1 << i)
        return result if result <= max_int else ~(result ^ mask)
        """
        leftmost = (result >> 31) & 1
        print(leftmost)
        result = (result & 0x7fffffff)
        print(result)
        result |= (leftmost << 31)
        """
        #return result if result != 2147483648 else -2147483648