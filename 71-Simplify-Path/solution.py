class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        result = ""
        n = len(path)
        i = 1
        while i < n:
            if path[i] != '/':
                temp = path[i]
                while i + 1 < n and path[i + 1] != '/':
                    temp += path[i + 1]
                    i += 1
                if temp == '..':
                    if stack:
                        stack.pop()
                elif temp != '.':
                    stack.append(temp)
            i += 1
        return "/" + '/'.join(stack)
       
