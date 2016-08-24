from collections import defaultdict
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = defaultdict(int)
        candidtates = set()
        for i, c in enumerate(s):
            if lookup[c]:
                candidtates.discard(lookup[c])
            else:
                lookup[c] = i + 1
                candidtates.add(i + 1)
        return min(candidtates) - 1 if candidtates else -1
        """
        maps = [[-1, 0] for i in range(26)]
        first = ''
        result = len(s)
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            maps[index][0] = i
            maps[index][1] += 1
        for pair in maps:
            if pair[1] == 1:
                result = min(result, pair[0])
        return result if result != len(s) else -1
        """