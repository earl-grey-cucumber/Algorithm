class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        dif = 1
        l = preorder.split(',')
        for c in l:
            dif -= 1
            if dif < 0:
                return False
            if c != '#':
                dif += 2
        return dif == 0