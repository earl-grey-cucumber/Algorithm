class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        for i in range(1, len(s)):
            if s[i] == '+' and s[i - 1] == '+':
                result.append(s[:i-1] + "--" + s[i+1:])
        return result