class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        stack = []
        last, max_len = -1, 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if not stack:
                    last = i
                else:
                    stack.pop()
                    if not stack:
                        max_len = max(max_len, i - last)
                    else:
                        max_len = max(max_len, i - stack[-1])
        return max_len
                        