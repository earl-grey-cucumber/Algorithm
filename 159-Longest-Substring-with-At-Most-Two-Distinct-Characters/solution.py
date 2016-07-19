class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        p, q, max_len, min_index = -1, -1, 1, -1
        for i in range(len(s)):
            if p == -1 or s[i] == s[p]:
                p = i
            elif q == -1 or s[i] == s[q]:
                q = i
            else:
                min_index = min(p, q)
                if min_index == p:
                    p = i
                else:
                    q = i
            max_len = max(max_len, i - min_index)
        return max_len
            