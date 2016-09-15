class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0 or denominator == 0:
            return "0"
        sign = (numerator > 0 and denominator > 0) or  (numerator < 0 and denominator < 0)
        result = ""
        if not sign:
            result += "-"
        up, down = abs(numerator), abs(denominator)
        remain = up % down
        result += str(up / down)
        if remain == 0:
            return result            
        result += "."
        mapping = {}
        i = len(result) # not i=2, result may be positive or negative, also may >= 10
        while remain != 0 and remain not in mapping:
            mapping[remain] = i
            result += str(remain * 10 / down)
            remain = (remain * 10) % down
            i += 1
        if remain == 0:
            return result
        result = result[0:mapping[remain]] + "(" + result[mapping[remain]:] # not i
        result += ")"
        return result
