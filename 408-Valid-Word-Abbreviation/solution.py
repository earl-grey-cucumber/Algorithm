class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, n, j = 0, len(abbr), 0
        while i < n and j < len(word):
            if abbr[i].isdigit():
                num = 0
                if abbr[i] == '0':
                    return False
                while i < n and abbr[i].isdigit():
                    num = num * 10 + ord(abbr[i]) - ord('0')
                    i += 1
                j += num
            else:
                if abbr[i] != word[j]:
                    return False
                i += 1
                j += 1
        return i == n and j == len(word)
                
            