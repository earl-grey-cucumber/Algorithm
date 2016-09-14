class TrieNode(object):
    def __init__(self, val=""):
        self.end = False
        self.children = dict()

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        n = len(word)
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]
        cur.end = True

    def search(self, word):
        n = len(word)
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        if cur.end:
            return True
        return False

    def startsWith(self, prefix):
        n = len(prefix)
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

class Solution(object):
    def findWords(self, board, words):
        if not board or not words:
            return []
        result = set()
        trie = Trie()
        for word in words:
            trie.insert(word)
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, trie.root, result, visited, i, j, "")
        return list(result)
        
    def dfs(self, board, cur, result, visited, x, y, path):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or visited[x][y]:
            return
        if board[x][y] not in cur.children:
            return
        next = cur.children[board[x][y]]
        path += board[x][y]
        if next.end: # find a whole word
            result.add(path)
        visited[x][y] = True
        self.dfs(board, next, result, visited, x + 1, y, path)
        self.dfs(board, next, result, visited, x - 1, y, path)
        self.dfs(board, next, result, visited, x, y + 1, path)
        self.dfs(board, next, result, visited, x, y - 1, path)
        visited[x][y] = False
