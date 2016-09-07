class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(result, mid, half, path, visited):
            if len(path) == len(half):
                cur = ''.join(path)
                result.append(cur + mid + cur[::-1])
                return
            for i in xrange(len(half)):
                if visited[i] or (i > 0 and half[i - 1] == half[i] and not visited[i - 1]):
                    continue
                visited[i] = True
                path.append(half[i])
                dfs(result, mid, half, path, visited)
                path.pop(-1)
                visited[i] = False
      
        maps = {}
        for c in s:
            if c not in maps:
                maps[c] = 0
            maps[c] += 1
        odd, mid, half =  False, "", ""
        for key in maps:
            if maps[key] % 2 == 1:
                if odd:
                    return []
                odd = True
                mid = key
                maps[key] -= 1
        print(mid)
        for key in maps:
            if maps[key] % 2 == 0:
                half += key * (maps[key] / 2)
        print(half)
        result, visited = [], [False for i in xrange(len(half))]
        dfs(result, mid, half, [], visited)
        return result