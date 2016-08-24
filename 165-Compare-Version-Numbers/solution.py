class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        m, n  = len(version1), len(version2)
        i, j = 0, 0
        while i < m or j < n:
            num1, num2 = 0, 0
            while i < m and version1[i] != '.':
                num1 = num1 * 10 + ord(version1[i]) - ord('0')
                i += 1
            while j < n and version2[j] != '.':
                num2 = num2 * 10 + ord(version2[j]) - ord('0')
                j += 1
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
            i += 1
            j += 1
        return 0