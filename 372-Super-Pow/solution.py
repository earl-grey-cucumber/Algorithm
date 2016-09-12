class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        result, base = 1, a
        for num in b[::-1]:
            result = (result * (base ** num) % 1337) % 1337
            base = (base ** 10) % 1337
        return result