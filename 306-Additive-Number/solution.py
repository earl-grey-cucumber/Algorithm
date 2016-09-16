class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def isValid(num, i, j):
            if num[0] == '0' and i > 1:
                return False
            if num[i] == '0' and j > 1:
                return False
            x = int(num[0:i])
            y = int(num[i:i+j])
            sumstr = ""
            start = i + j
            while start < len(num):
                y = y + x
                x = y - x
                sumstr = str(y)
                if not num.startswith(sumstr, start, len(num)):
                    return False
                start += len(sumstr)
            return True
        i, n = 1, len(num)
        while i <= n / 2 + 1:
            j = 1
            while max(j, i) <= n - i - j:
                if isValid(num, i, j):
                    return True
                j += 1
            i += 1
        return False
    