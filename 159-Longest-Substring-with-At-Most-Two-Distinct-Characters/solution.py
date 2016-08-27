class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j, max_len, count = 0, 0, 0, 0
        maps = {}
        for i in xrange(len(s)):
            if s[i] not in maps:
                maps[s[i]] = 0
            maps[s[i]] += 1
            if maps[s[i]] == 1:
                count += 1
                while count > 2:
                    maps[s[j]] -= 1
                    if maps[s[j]] == 0:
                        count -= 1
                    j += 1
            max_len = max(max_len, i - j + 1)
        return max_len