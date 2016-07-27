class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result, queue, visited = [], [s], set()
        visited.add(s)
        found = False
        while queue:
            cur = queue.pop(0)
            if self.isValid(cur):
                found = True
                result.append(cur)
            if found:
                continue
            for i in range(len(cur)):
                if cur[i] == '(' or cur[i] == ')':
                    temp = cur[0: i] + (cur[i + 1:] if i < len(cur) - 1 else "")
                    if temp not in visited:
                        visited.add(temp)
                        queue.append(temp)
                        found = False
        return result
    
    def isValid(self, cur):
        left, right = 0, 0
        for i in range(len(cur)):
            if cur[i] == '(':
                left += 1 
            elif cur[i] == ')':
                right += 1
            if left < right:
                return False
        return left == right
    
    
    