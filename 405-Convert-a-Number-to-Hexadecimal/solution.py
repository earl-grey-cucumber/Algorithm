class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        if num < 0:
            num += (2 ** 32)
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        result = ""
        while num > 0:
            """
            cur = num % 16
            result = digits[cur] + result
            num = (num - cur) / 16
            """
            result = digits[num & 15] + result
            num = (num >> 4)
        return result.lstrip('0')