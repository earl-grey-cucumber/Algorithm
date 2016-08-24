class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        i, j = len(s) - 1, len(s) - 1
        while i >= 0:
            while i >= 0 and s[i] == ' ':
                i -= 1
            j = i
            while i > 0 and s[i - 1] != ' ':
                i -= 1
            if i < 0:
                break
            if len(result) == 0:
                result += s[i:j+1]
            else:
                result += " " + s[i:j+1]
            i -= 1
        return result