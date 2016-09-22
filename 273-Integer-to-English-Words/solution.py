class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def helper(cur):
            less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
            tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            if cur == 0:
                return ""
            if cur < 20:
                return less_than_20[cur] + " "
            elif cur < 100:
                return tens[cur / 10] + " " + helper(cur % 10)
            else:
                return less_than_20[cur / 100] + " Hundred " + helper(num % 100)
                
        if num == 0:
            return "Zero"
        thousands = ["", "Thousand", "Million", "Billion"]
        result = ""
        i = 0
        while num > 0:
            if num % 1000 != 0:
                result = helper(num % 1000) + thousands[i] + " " + result
            i += 1
            num /= 1000
        return result.strip(" ")
