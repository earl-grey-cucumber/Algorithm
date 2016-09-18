class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        visited = [False for i in range(9)]
        count = 0
        for i in range(m, n + 1):
            count += self.dfs(-1, i, visited)
            visited = [False for i in range(9)]
        return count
        
    def dfs(self, last, len, visited):
        if len == 0:
            return 1
        sum = 0
        for i in range(9):
            if self.isValid(last, i, visited):
                visited[i] = True
                sum += self.dfs(i, len - 1, visited)
                visited[i] = False
        return sum
    
    def isValid(self, last, cur, visited):
        if visited[cur]:
            return False
        if last == -1:
            return True
        if (last + cur) % 2 == 1:
            return True
        mid = (last + cur) / 2
        if mid == 4:
            return visited[mid]
        if (last % 3 != cur % 3) and (last / 3 != cur / 3):
            return True
        return visited[mid]