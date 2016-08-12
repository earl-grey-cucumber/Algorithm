class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        bits = [0 for i in range(n)]
        for i in range(n):
            for j in range(len(words[i])):
                bits[i] |= (1 << (ord(words[i][j]) - ord('a')))
        result = 0
        for i in range(n):
            for j in range(i + 1, n):
                if bits[i] & bits[j] == 0:
                    result = max(result, len(words[i]) * len(words[j]))
        return result
            