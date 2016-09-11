class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        unique = set()
        graph = {}
        for word in words:
            for k in range(len(word)):
                unique.add(word[k])
        for c in unique:
            graph[c] = []
        for i in range(1, len(words)):
            for j in range(len(words[i])):
                if j >= len(words[i - 1]):
                    break
                if words[i - 1][j] == words[i][j]:
                    continue
                graph[words[i - 1][j]].append(words[i][j])
                break
        result = [] # str can’t be passed by address
        visited = set()
        for c in unique:
            if not self.dfs(c, graph, result, [], visited):
                return ""
        return ''.join(result)[::-1]
        
    def dfs(self, c, graph, result, path, visited):
        if c in path:
            return False
        if len(visited) == len(graph):
            return True
        if c not in visited:
            visited.add(c)
            path.append(c)
            for nei in graph[c]:
                if not self.dfs(nei, graph, result, path, visited):
                    return False
            path.pop(-1)
            result.append(c)
        return True