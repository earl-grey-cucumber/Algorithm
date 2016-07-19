class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s), len(t)
        if abs(m - n) >= 2:
            return False
        if m < n:
            return self.isOneEditDistance(t, s)
        i = 0
        while i < n and s[i] == t[i]:
            i += 1
        if i == m:
            return False
        if m - n == 1:
            while i < n and s[i + 1] == t[i]:
                i += 1
        else:
            i += 1
            while i < n and s[i] == t[i]:
                i += 1
        return i == n