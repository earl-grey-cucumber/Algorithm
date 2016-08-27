class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        def encode(s):
            code = "0"
            for i in range(1, len(s)):
                dif = (ord(s[i]) - ord(s[i - 1]) + 26) % 26
                code += str(dif)
            return code
        maps = {}
        for s in strings:
            code = encode(s)
            if code not in maps:
                maps[code] = []
            maps[code].append(s)
        return maps.values()
            