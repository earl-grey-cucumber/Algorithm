class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, sign, i, n, num = 0, 1, 0, len(s), 0
        stack = []
        while i < n:
            c = s[i]
            if c.isdigit():
                num = int(s[i])
                while i + 1 < n and s[i + 1].isdigit():
                    num = num * 10 + int(s[i + 1])
                    i += 1
            elif c == "+":
                result += sign * num
                num, sign = 0, 1
            elif c == "-":
                result += sign * num
                num, sign = 0, -1
            elif c == "(":
                stack.append(result)
                stack.append(sign)
                result, sign = 0, 1
            elif c == ")":
                result += sign * num
                result *= stack.pop(-1)
                result += stack.pop(-1)
                num = 0
            i += 1
        if num:
            result += sign * num
        return result
                
            