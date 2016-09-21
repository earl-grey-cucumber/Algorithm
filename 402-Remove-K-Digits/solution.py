class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for digit in num:
            while k and stack and digit < stack[-1]:
                stack.pop(-1)
                k -= 1
            stack.append(digit)
        while k:
            stack.pop(-1)
            k -= 1
        result = "".join(stack).lstrip("0")
        return result if result != "" else "0"