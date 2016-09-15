class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        count = [0 for i in range(n + 1)]
        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1
        cur = 0
        for i in range(n, -1, -1):
            cur += count[i]
            if cur >= i:
                return i
        return 0
        
     