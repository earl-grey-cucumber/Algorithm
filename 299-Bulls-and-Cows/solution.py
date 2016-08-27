class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        size = len(secret)
        bulls = 0
        count1, count2 = [0]*10, [0]*10
        for i in xrange(size):
            if secret[i] == guess[i]:
                bulls += 1
            count1[int(secret[i])]+=1
            count2[int(guess[i])]+=1
        for j in xrange(10):
            count1[j] = min(count1[j], count2[j])
        cow = sum(count1) - bulls   
        return str(bulls) + "A" + str(cow) + "B"