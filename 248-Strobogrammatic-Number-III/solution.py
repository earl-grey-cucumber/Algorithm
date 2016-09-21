class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        def dfs(nums, count, low, high, cur, left, right):
            if left > right:
                temp = ''.join(cur)
                if (len(cur) == len(low) and int(temp) < int(low)) or (len(cur) == len(high) and int(temp) > int(high)):
                    return
                count[0] += 1
                return
            for pair in nums:
                cur[left], cur[right] = pair[0], pair[1]
                if len(cur) != 1 and cur[0] == '0':
                    continue
                if left < right or (left == right and pair[0] == pair[1]):
                    dfs(nums, count, low, high, cur, left + 1, right - 1)
        nums = [['0', '0'], ['1', '1'], ['6', '9'], ['8', '8'], ['9', '6']]
        count = [0]
        for i in range(len(low), len(high) + 1):
            cur = ['' for j in range(i)]
            dfs(nums, count, low, high, cur, 0, i - 1)
        return count[0]