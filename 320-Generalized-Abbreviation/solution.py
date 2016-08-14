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
            for j in range(n):
                if (i >> j) & 1:
                    count += 1 
                else:
                    if count:
                        path += str(count)
                    path += word[j]
                    count = 0
            if count:
                path += str(count)
            result.append(path)
        return result