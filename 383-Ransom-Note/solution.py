class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        maps = [0 for i in range(26)]
        for c in magazine:
            maps[ord(c) - ord('a')] += 1
        for c in ransomNote:
            index = ord(c) - ord('a')
            maps[index] -= 1
            if maps[index] < 0:
                return False
        return True
