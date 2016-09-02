class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        mapping = {}
        result = []
        for i in range(len(words)):
            mapping[words[i]] = i
        for i in range(len(words)):
            word = words[i]
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]
                if suffix == suffix[::-1] and prefix[::-1] in mapping and mapping[prefix[::-1]] != i:
                    result.append([i, mapping[prefix[::-1]]])
                if j > 0 and prefix == prefix[::-1] and suffix[::-1] in mapping and mapping[suffix[::-1]] != i:
                    result.append([mapping[suffix[::-1]], i])
        return result
