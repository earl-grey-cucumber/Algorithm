class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        low, high, result = 0, n - 1, 0
        while low <= high:
            mid = (low + high) / 2
            if citations[mid] >= n - mid:
                result = max(result, n - mid)
                high = mid - 1
            else:
                low = mid + 1
        return result
