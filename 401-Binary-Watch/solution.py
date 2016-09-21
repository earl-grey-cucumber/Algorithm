class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def helper(visited):
            hour, minute = 0, 0
            for i in range(4):
                if visited[i] == 1:
                    hour += (int)(2**i)
            for i in range(4, 10):
                if visited[i] == 1:
                    minute += (int)(2**(i - 4))
            if hour >= 12 or minute >= 60:
                return ""
            result = str(hour) + ":"
            if minute < 10:
                result += "0"
            result += str(minute)
            return result
        def dfs(num, result, k, index, visited):
            if k == num:
                cur = helper(visited)
                if cur != "":
                    result.append(cur)
                return
            if index == len(visited):
                return 
            visited[index] = 0
            dfs(num, result, k, index + 1, visited)
            visited[index] = 1
            dfs(num, result, k + 1, index + 1, visited)
            visited[index] = 0
        result = []
        visited = [0] * 10
        dfs(num, result, 0, 0, visited)
        return result