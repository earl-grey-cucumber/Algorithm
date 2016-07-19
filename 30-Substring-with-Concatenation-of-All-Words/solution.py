class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        maps = {}
        for word in words:
            if word not in maps:
                maps[word] = 1
            else:
                maps[word] += 1
        m, n, l = len(words), len(words[0]), len(s)
        result = []
        i = 0
        while i <= l - m * n + 1:
            found = {}
            j = 0
            while j < m:
                cur = s[i + j * n: i + j * n + n]   
                if cur not in maps:
                    break
                if cur not in found:
                    found[cur] = 0
                found[cur] += 1
                if found[cur] > maps[cur]:
                    break
                j += 1
            if j == m:
                result.append(i)
            i += 1
        return result