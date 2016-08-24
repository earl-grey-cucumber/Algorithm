class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        temp = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and temp[i] not in vowel:
                i += 1
            while i < j and temp[j] not in vowel:
                j -= 1
            temp[i], temp[j] = temp[j], temp[i]
            i += 1
            j -= 1
        return "".join(temp)