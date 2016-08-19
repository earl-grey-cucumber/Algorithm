# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, cand = 1, 0
        while i < n:
            if knows(cand, i):
                cand = i
            i += 1
        for i in range(n):
            if i == cand:
                continue
            if knows(cand, i):
                return -1
            if not knows(i, cand):
                return -1
        return cand
        