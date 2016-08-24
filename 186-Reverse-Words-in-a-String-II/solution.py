class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        def reverse(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        i, n = 0, len(s)
        while i < n:
            j = i
            while i + 1 < n and s[i + 1] != ' ':
                i += 1
            reverse(s, j, i)
            i += 2
        reverse(s, 0, n - 1)
            