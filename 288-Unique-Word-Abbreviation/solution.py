class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.maps = {}
        for word in dictionary:
            code = self.encode(word)
            if code not in self.maps:
                self.maps[code] = []
            self.maps[code].append(word)
            
    def encode(self, word):
        if len(word) <= 2:
            return word
        return word[0] + str(len(word) - 2) + word[-1]
        
    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if len(word) < 2:
            return True
        code = self.encode(word)
        if code not in self.maps:
            return True
        if len(self.maps[code]) == 1 and self.maps[code][0] == word:
            return True
        return False


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")