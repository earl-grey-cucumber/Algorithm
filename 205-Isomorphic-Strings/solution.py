class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        map1, map2 = {}, {}
        for i in range(len(s)):
            c = s[i]
            if c in map1 and map1[c] != t[i]:
                return False
            if t[i] in map2 and map2[t[i]] != c:
                return False
            map1[c] = t[i]
            map2[t[i]] = c
        return True