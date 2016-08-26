class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i, j, result = -1, -1, len(words)
        for k in xrange(len(words)):
            if words[k] == word1:
                i = k
            if words[k] == word2:
                j = k
            if i != -1 and j != -1:
                result = min(result, abs(i - j))
        return result