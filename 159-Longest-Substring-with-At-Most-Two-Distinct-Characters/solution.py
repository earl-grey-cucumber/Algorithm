class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        p, q, max_len, min_index = -1, -1, 0, -1
        for i in xrange(len(s)):
            if p == -1 or s[i] == s[p]:
                p = i
            elif q == -1 or s[i] == s[q]:
                q = i
            elif s[i] != s[p] and s[i] != s[q]:
                min_index = min(p, q)
                if p < q:
                    p = i
                else:
                    q = i
            max_len = max(max_len, i - min_index)
        return max_len