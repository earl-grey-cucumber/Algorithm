class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        result = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i] != "#":
                    num = num * 10 + int(s[i])
                    i += 1
                i += 1
                cur = s[i: i + num]
                result.append(cur)
            i += num
        return result

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))