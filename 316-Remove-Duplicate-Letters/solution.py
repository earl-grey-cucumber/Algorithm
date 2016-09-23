class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(maps):
            min_pos = sys.maxint
            for key in maps.keys():
                min_pos = min(min_pos, maps[key])
            return min_pos
        if len(s) <= 1:
            return s
        maps = {}
        for i in range(len(s)):
            maps[s[i]] = i
        result = [''] * len(maps)
        begin, end = 0, helper(maps)
        for i in range(len(result)):
            min_char = None
            for j in range(begin, end + 1):
                if s[j] in maps and (min_char is None or ord(s[j]) < ord(min_char)):
                    min_char = s[j]
                    begin = j + 1
            result[i] = min_char
            if i == len(result) - 1:
                break
            del maps[min_char]
            if s[end] == min_char:
                end = helper(maps)
        return ''.join(result)
     