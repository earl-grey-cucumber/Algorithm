class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        xor = 0
        for c in s + t:
            xor ^= ord(c) - ord('a')
        return chr(xor + ord('a'))