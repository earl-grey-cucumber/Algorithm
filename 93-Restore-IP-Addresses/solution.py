class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4 or len(s) > 12:
            return []
        result = []
        self.dfs(s, result, "", 0)
        return result
        
    def dfs(self, s, result, path, count):
        if count == 3:
            if self.isValid(s):
                result.append(path + s)
            return
        i = 1
        while i <= 3 and i < len(s):
            cur = s[: i]
            if self.isValid(cur):
                self.dfs(s[i:], result, path + cur + ".", count + 1)
            i += 1
    
    def isValid(self, cur):
        if cur[0] == '0':
            return cur == "0"
        return 0 < int(cur) <= 255
    