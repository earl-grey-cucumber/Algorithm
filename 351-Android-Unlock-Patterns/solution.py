class Solution(object):
    def numberOfPatterns(self, m, n):
        def dfs(visited, skip, cur, remain):
            if remain < 0:
                return 0
            if remain == 0:
                return 1
            visited[cur] = True
            count = 0
            for i in range(1, 10):
                if not visited[i] and (skip[cur][i] == 0 or visited[skip[cur][i]]):
                    count += dfs(visited, skip, i, remain - 1)
            visited[cur] = False
            return count
            
        skip = [[0 for i in range(10)] for j in range(10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5
        visited = [False] * 10
        result = 0
        for i in range(m, n + 1):
            result += dfs(visited, skip, 1, i - 1) * 4
            result += dfs(visited, skip, 2, i - 1) * 4
            result += dfs(visited, skip, 5, i - 1)
        return result
        
    """
    def numberOfPatterns(self, m, n):
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
    """