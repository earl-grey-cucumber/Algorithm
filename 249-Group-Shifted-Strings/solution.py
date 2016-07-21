class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        def encode(s):
            if not s:
                return ""
            encoded = ""
            for i in range(1, len(s)):
                diff = (ord(s[i]) - ord(s[i - 1]) + 26) % 26
                encoded += str(diff) + "#"
            return encoded
                
        maps = collections.defaultdict(list)
        result = []
        for s in strings:
            encoded = encode(s)
            maps[encoded].append(s)
        for key, value in maps.items():
            result.append(value)
        return result