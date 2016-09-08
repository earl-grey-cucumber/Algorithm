class Solution(object):
    def getFactors(self, n):
        todo, combis = [(n, 2, [])], []
        while todo:
            n, i, combi = todo.pop()
            while i * i <= n:
                if n % i == 0:
                    combis += combi + [i, n/i],
                    todo += (n/i, i, combi+[i]),
                i += 1
        return combis
        
        """
        def factor(n, i, combi, combis):
            while i * i <= n:
                if n % i == 0:
                    combis += combi + [i, n/i],
                    factor(n/i, i, combi+[i], combis)
                i += 1
            return combis
        return factor(n, 2, [], [])
        """
        
        """
        def dfs(index, result, path, cur):
            if cur == 1:
                result.append(path[:])
                return
            for i in range(index, n):
                if i > cur:
                    return
                if cur % i != 0:
                    continue
                dfs(i, result, path + [i], cur)
        if n <= 1:
            return []
        result = []
        dfs(2, result, [], n)
        return result
        """