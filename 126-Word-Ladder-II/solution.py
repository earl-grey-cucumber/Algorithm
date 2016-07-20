from collections import defaultdict
class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        graph, visited, result = defaultdict(list), {}, []
        self.bfs(beginWord, endWord, wordlist, graph, visited)
        self.dfs(beginWord, endWord, graph, visited, result, [])
        return result
        
    def bfs(self, beginWord, endWord, wordlist, graph, visited):
        q = [endWord]
        visited[endWord] = 0
        while q:
            cur = q.pop(0)
            neighbors = self.get_n(cur, wordlist)
            for neighbor in neighbors:
                graph[neighbor].append(cur)
                if neighbor not in visited:
                    visited[neighbor] = visited[cur] + 1
                    q.append(neighbor)  
 
    def get_n(self, cur, wordlist):
        result = []
        for j in range(len(cur)):
            temp = list(cur)
            for i in range(26):
                temp[j] = chr(ord('a') + i)
                newWord = ''.join(temp)
                if newWord != cur and newWord in wordlist:
                    result.append(newWord)
        return result
        
    def dfs(self, cur, endWord, graph, visited, result, path):
        path.append(cur)
        if cur == endWord:
            result.append(path[:])
            path.pop(-1)  
            return result
        for neighbor in graph[cur]:
            if visited[neighbor] + 1 == visited[cur]:
                self.dfs(neighbor, endWord, graph, visited, result, path)
        path.pop(-1)  