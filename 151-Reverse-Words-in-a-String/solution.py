class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #return ' '.join(reversed(s.split( )))
        result = ""
        n = len(s)
        i, j = n - 1, n - 1
        while i >= 0:
            while i >= 0 and s[i] == ' ':
                i -= 1
            j = i
            while i > 0 and s[i - 1] != ' ':
                i -= 1
            if i < 0:
               return result
            if not result:
                result += s[i: j + 1]
            else:
                result += " " + s[i: j + 1]
            i -= 1
        return result