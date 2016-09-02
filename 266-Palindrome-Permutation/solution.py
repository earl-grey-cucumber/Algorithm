class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        visited = set()
        for c in s:
            if c not in visited:
                visited.add(c)
            else:
                visited.remove(c)
        return len(visited) <= 1
            