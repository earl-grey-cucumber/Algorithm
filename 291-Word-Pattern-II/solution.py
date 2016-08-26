class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        maps = {}
        visited = set()
        return self.isMatch(str, 0, pattern, 0, maps, visited)
    
    def isMatch(self, str, i, pat, j, maps, visited):
        if i == len(str) and j == len(pat):
            return True
        if i == len(str) or j == len(pat):
            return False
        c = pat[j]
        if c in maps:
            s = maps[c]
            if not str.startswith(s, i):
                return False
            return self.isMatch(str, i + len(s), pat, j + 1, maps, visited)
        else:
            for k in range(i, len(str)):
                p = str[i: k + 1]
                if p in visited:
                    continue
                maps[c] = p
                visited.add(p)
                if self.isMatch(str, k + 1, pat, j + 1, maps, visited):
                    return True
                del maps[c]
                visited.remove(p)
            return False