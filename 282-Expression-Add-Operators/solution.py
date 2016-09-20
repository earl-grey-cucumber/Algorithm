class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def dfs(result, path, num, target, index, val, temp):
            if index == len(num):
                if val == target:
                    result.append(path)
                    return
            for i in range(index, len(num)):
                if i != index and num[index] == '0':
                    break
                cur = int(num[index: i + 1])
                if index == 0:
                    dfs(result, path + str(cur), num, target, i + 1, cur, cur)
                else:
                    dfs(result, path + "+" + str(cur), num, target, i + 1, val + cur, cur)
                    dfs(result, path + "-" + str(cur), num, target, i + 1, val - cur, -cur)
                    dfs(result, path + "*" + str(cur), num, target, i + 1, val - temp + cur * temp, cur * temp)
                
        result = []
        if not num:
            return result
        dfs(result, "", num, target, 0, 0, 0)
        return result
