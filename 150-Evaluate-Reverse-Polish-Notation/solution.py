class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
        stack = []
        ops = ["+", "-", "*", "/"]
        for i in range(len(tokens)):
            if tokens[i] not in ops:
                stack.append(int(tokens[i]))
            else:
                num1 = stack.pop(-1)
                num2 = stack.pop(-1)
                op = tokens[i]
                if op == "+":
                    stack.append(num2 + num1)
                elif op == "-":
                    stack.append(num2 - num1)
                elif op == "*":
                    stack.append(num2 * num1)
                else:
                    stack.append(int(float(num2) / num1))
        return stack.pop(0)
