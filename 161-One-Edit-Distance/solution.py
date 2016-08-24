class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if abs(len(s) - len(t)) > 1:
            return False
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)
        i, m, n = 0, len(s), len(t)
        while i < m and s[i] == t[i]:
            i += 1
        if i == m:
            return n == m + 1
        if m == n:
            i += 1
            while i < m and s[i] == t[i]:
                i += 1
        else:
            while i < m and s[i] == t[i + 1]:
                i += 1
        return i == m