class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        maps = {}
        for c in s:
            if c not in maps:
                maps[c] = 0
            maps[c] += 1
        for c in t:
            if c not in maps:
                return False
            maps[c] -= 1
            if maps[c] == 0:
                del maps[c]
        return len(maps) == 0