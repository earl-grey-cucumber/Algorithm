class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        maps = {}
        for c in s:
            if c not in maps:
                maps[c] = 0
            maps[c] += 1
        odd = False
        for key in maps:
            if maps[key] % 2 == 1:
                if odd:
                    return False
                odd = True
        return True
            