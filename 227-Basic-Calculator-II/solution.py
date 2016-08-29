class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, i, temp, isNeg = 0, 0, 1, False
        while i < len(s):
            c = s[i]
            if c == ' ':
                i += 1
                continue
            if c.isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + ord(s[i]) - ord('0')
                    i += 1
                if not isNeg:
                    temp *= num
                else:
                    temp = (int)(float(temp) / num)
            else:
                isNeg = False
                if c == "+":
                    result += temp
                    temp = 1
                elif c == "-":
                    result += temp
                    temp = -1
                elif c == "/":
                    isNeg = True
                i += 1
        result += temp
        return result