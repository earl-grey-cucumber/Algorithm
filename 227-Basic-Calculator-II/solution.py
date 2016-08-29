class Solution(object):
    def calculate(self, s):
        stack = []
        num, result, n, i = 0, 0, len(s), 0
        sign = '+'
        while i < n:
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            if i == n - 1 or (not s[i].isdigit() and s[i] != ' '):
                if sign == '-':
                    stack.append(-1 * num)
                elif sign == '+':
                    stack.append(num)
                elif sign == '*':
                    stack.append(stack.pop(-1) * num)
                else:
                    stack.append((int)((float)(stack.pop(-1)) / num))
                sign = s[i]
                num = 0
            i += 1
        result, size = 0, len(stack)
        for j in stack:
            result += j
        return result