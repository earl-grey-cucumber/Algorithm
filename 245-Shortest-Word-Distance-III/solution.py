class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i, j, result = -1, -1, len(words)
        for k, word in enumerate(words):
            if word1 == word2 and word == word2:
                if i < j:
                    i = k
                else:
                    j = k
            elif word == word1:
                i = k
            elif word == word2:
                j = k
            if i != -1 and j != -1:
                result = min(result, abs(i - j))
        return result
        