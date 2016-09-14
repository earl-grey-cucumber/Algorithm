from random import randint
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vti, self.itv = {}, []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.vti:
            return False
        self.vti[val] = len(self.vti)
        self.itv.append(val)
        return True
        
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.vti:
            return False
        i = self.vti[val]
        size = len(self.vti)
        if i < size - 1:
            new_val = self.itv[size - 1]
            self.itv[i] = new_val
            self.vti[new_val] = i
        self.itv.pop(-1)
        del self.vti[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        r = randint(0, len(self.itv) - 1)
        return self.itv[r]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()