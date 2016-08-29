class Solution(object):
    def isPerfectSquare(self, num):
        if num <= 1:
            return num == 1
        """
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0
        """
        
        low, high = 0, num - 1
        while low <= high:
            mid = low + (high - low) / 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid + 1
            else:
                high = mid - 1
        return False