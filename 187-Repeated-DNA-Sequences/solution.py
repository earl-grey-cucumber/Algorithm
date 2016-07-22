class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 10:
            return []
        maps = {}
        dictionary = {'A': 0, "C": 1, 'G': 2, 'T':3}
        cur = 0
        result = []
        mask = (1 << 18) - 1
        for i in range(10):
            cur = (cur << 2) | dictionary[s[i]]
        maps[cur] = 1
        for i in range(10, len(s)):
            cur = ((cur & mask) << 2) | dictionary[s[i]]
            if cur not in maps:
                maps[cur] = 1
            else:
                maps[cur] += 1
            if maps[cur] == 2:
                result.append(s[i - 9: i + 1])
        return result