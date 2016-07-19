class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, result, temp = 0, 0, 1
        divide = False
        while i < len(s):
            c = s[i]
            if '0' <= c <= '9':
                num = int(c)
                while i + 1 < len(s) and '0' <= s[i + 1] <= '9':
                    num = num * 10 + int(s[i + 1])
                    i += 1
                if divide:
                    temp = (int)(float(temp) / num)
                else:
                    temp *= num
            elif c == "+" or c == "-" or c == "*" or c == "/":
                divide = False
                if c == "/":
                    divide = True
                elif c == "+": 
                    result += temp
                    temp = 1
                elif c == "-":
                    result += temp
                    temp = -1
            i += 1
        result += temp
        return result