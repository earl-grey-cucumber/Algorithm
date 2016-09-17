class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def helper(input, l, h):
            result = []
            if l > h:
                return []
            hasOp = False
            for i in range(l, h + 1):
                if input[i] == '+' or input[i] == "-" or input[i] == '*':
                    hasOp = True
                    left = helper(input, l, i - 1)
                    right = helper(input, i + 1, h)
                    for j in range(len(left)):
                        for k in range(len(right)):
                            if input[i] == "+":
                                result.append(left[j] + right[k])
                            elif input[i] == "-":
                                result.append(left[j] - right[k])
                            elif input[i] == "*":
                                result.append(left[j] * right[k])
            if not hasOp:
                result.append(int(input[l:h+1]))
            return result
        return helper(input, 0, len(input) - 1)