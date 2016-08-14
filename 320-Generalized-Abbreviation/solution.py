class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        n = len(word)
        result = []
        for i in range(1 << n):
            path = ""
            count = 0
            for j in range(n + 1):
                if (i >> j) & 1:
                    count += 1 
                else:
                    if count:
                        path += str(count)
                    if j == n:
                        continue
                    path += word[j]
                    count = 0
            result.append(path)
        return result