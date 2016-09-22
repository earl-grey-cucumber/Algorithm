class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def helper(s, maps):
            if s in maps:
                return maps[s]
            for i in range(len(s) - 1):
                if s[i:i + 2] == "++":
                    oppo = s[:i] + "--" + s[i + 2:]
                    if not helper(oppo, maps):
                        maps[s] = True
                        return True
            maps[s] = False
            return False
        if len(s) < 2:
            return False
        maps = {}
        return helper(s, maps)