from collections import defaultdict
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        maps = defaultdict(int)
        for c in s:
            maps[c] += 1
        count = 0
        odd = False
        for key, value in maps.items():
            if value % 2 == 0:
                count += value
            elif not odd:
                count += value
                odd = True
            else:
                count += value - 1
        return count