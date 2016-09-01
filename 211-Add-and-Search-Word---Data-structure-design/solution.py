class TrieNode(object):
    def __init__(self, c):
        self.val = c
        self.children = dict()
        self.end = False

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode("")

    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]
        cur.end = True
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def helper(word, index, cur):
            if index == len(word):
                return cur.end
            if word[index] == '.':
                for c in cur.children:
                    if helper(word, index + 1, cur.children[c]):
                        return True
            if word[index] in cur.children:
                return helper(word, index + 1, cur.children[word[index]])
            return False

        return helper(word, 0, self.root)
        
# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")