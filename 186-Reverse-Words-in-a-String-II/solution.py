class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        n = len(s)
        i, j = n - 1, n - 1
        while j >= 0:
            while j > 0 and s[j - 1] != ' ':
                j -= 1
            self.reverse_s(s, j, i)
            j -= 2
            i = j
        self.reverse_s(s, 0, len(s) - 1)
        
    def reverse_s(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
