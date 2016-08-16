class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.count = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number not in self.count:
            self.count[number] = 1
        else:
            self.count[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.count:
            if value - num in self.count:
                if num * 2 == value and self.count[num] == 1:
                    continue
                else:
                    return True
        return False


# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)