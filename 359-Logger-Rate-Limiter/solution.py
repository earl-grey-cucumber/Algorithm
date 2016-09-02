class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log = {}
        

    def shouldPrintMessage(self, timestamp, message):
        if timestamp < self.log.get(message, 0):
            return False
        self.log[message] = timestamp + 10
        return True
        """
        if message not in self.log:
            self.log[message] = [timestamp]
            return True
        else:
            if self.log[message][-1] == timestamp:
                return False
            prev = self.log[message][0]
            if timestamp - prev >= 10:              
                self.log[message] = [timestamp] # latest occurrence is the timestamp
                return True
            else:
                self.log[message].append(timestamp)
                return False  
        """


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)