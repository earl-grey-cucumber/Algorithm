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
        min_dist = sys.maxint
        for i in range(len(list2)):
            dist = self.helper(list2[i], list1)
            if dist < min_dist:
                min_dist = dist
        return min_dist 
    
    # for a target, find the closest values’(bigger / smaller) index in list1
    def helper(self, target, list1):
        n = len(list1)
        left, right, low, high = -1, n, 0, n - 1 # left = -1, if left = n, for(0, [0]), left = max(left,0), left keeps to be n
        while low <= high:
            mid = (low + high) / 2
            if list1[mid] <= target:
                left = max(left, mid)
                low = mid + 1
            else:
                high = mid - 1
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) / 2
            if list1[mid] >= target:
                right = min(right, mid)
                high = mid - 1
            else:
                low = mid + 1
        if left != -1 and right != n:
            return min(target - list1[left], list1[right] - target)
        if left != -1:
            return target - list1[left]
        else:
            return list1[right] - target
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
        """
            

# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")