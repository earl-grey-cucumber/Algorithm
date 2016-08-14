class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        first = 0
        count = {}
        result = set()
        mask = (1 << 18) - 1
        mapping = {"A": 0, "C": 1, "G": 2, "T":3}
        for i in range(10):
            first = (first << 2) | mapping[s[i]]
        count[first] = 1
        cur = first
        for i in range(10, len(s)):
            cur = ((cur & mask) << 2) | mapping[s[i]]
            if cur not in count:
                count[cur] = 1
            else:
                count[cur] += 1
                if count[cur] == 2: # if add all count[cur] > 1 to result, will MLE
                    result.add(s[i - 9: i + 1])
        return list(result)
