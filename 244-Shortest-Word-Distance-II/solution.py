class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.maps = {}
        for i, word in enumerate(words):
            if word not in self.maps:
                self.maps[word] = []
            self.maps[word].append(i)

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        list1, list2 = self.maps[word1], self.maps[word2]
        mindis = sys.maxint
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            cand1 = list1[i] 
            cand2 = list2[j]
            mindis = min(mindis, abs(cand1 - cand2))
            if cand1 == cand2:
                return 0
            elif cand1 < cand2:
                i += 1
            else:
                j += 1
        return mindis
            

# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")