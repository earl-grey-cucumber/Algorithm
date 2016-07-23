class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bows = 0
        cows = 0
        m, n = len(secret), len(guess)
        count1 = [0] * 10
        count2 = [0] * 10
        for i in range(m):
            if secret[i] == guess[i]:
                bows += 1
            count1[int(secret[i]) - 1] += 1
            count2[int(guess[i]) - 1] += 1
        for i in range(10):
            cows += min(count1[i], count2[i])
        return str(bows) + "A" + str(cows - bows) + "B"
            
            