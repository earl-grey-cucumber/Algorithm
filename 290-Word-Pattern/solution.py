class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dict1, dict2 = {}, {}
        strs = str.split(" ")
        if len(pattern) != len(strs):
            return False
        for i in range(len(pattern)):
            c = pattern[i]
            s = strs[i]
            if c in dict1 and dict1[c] != s:
                return False
            if s in dict2 and dict2[s] != c:
                return False
            dict1[c] = s
            dict2[s] = c
        return True
