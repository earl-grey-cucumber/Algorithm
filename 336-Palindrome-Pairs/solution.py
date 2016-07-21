class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        result = []
        maps = {}
        for i, word in enumerate(words):
            maps[word] = i
        for i in range(len(words)):
            word = words[i]
            for j in range(len(word) + 1):
                pre = word[:j]
                suf = word[j:]
                if suf == suf[::-1] and pre[::-1] in maps and maps[pre[::-1]] != i:
                    result.append([i, maps[pre[::-1]]])
                if j > 0 and pre == pre[::-1] and suf[::-1] in maps and maps[suf[::-1]] != i:
                    result.append([maps[suf[::-1]], i])
        return result