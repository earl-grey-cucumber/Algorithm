from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or k == 0:
            return 0
        i, j, n, result = 0, 0, len(s), 0
        maps = defaultdict(int)
        while j < n:
            if s[j] in maps or len(maps) < k:
                maps[s[j]] += 1
            else: 
                maps[s[j]] = 1
                while i < j and len(maps) > k:
                    maps[s[i]] -= 1
                    if maps[s[i]] == 0:
                        del maps[s[i]]
                    i += 1
            result = max(result, j - i + 1)
            j += 1
   
        return result