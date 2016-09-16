class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def helper(n, result, maps, cur, keys):
            if len(cur) == n:
                result.append(cur)
                return
            for i in range(len(keys)):
                c = keys[i]
                k = len(cur)
                if k + 1 == n:
                    if c in ['0', '1', '8']:
                        helper(n, result, maps, cur[0:k/2] + c + cur[k/2:], keys)
                else:
                    if c == "0" and (k + 2 == n or k + 3 == n):
                        continue
                    helper(n, result, maps,  c + cur + maps[c], keys)
        """                
        for i in range(len(cand)):
            num = cand[i]
            if k + 1 == n:
                if num == "0" or num == "1" or num == "8":
                    self.helper(result, dic, n, k + 1, path[0: k/2] + num + path[k/2:], cand)
            else:
                if (k + 2 == n or k + 3 == n) and num == "0":
                    continue
                self.helper(result, dic, n, k + 2, num + path + dic[num], cand)
        """       
        maps = {"0":"0", "1": "1", "6":"9", "8":"8", "9":"6"}
        keys = ['0', '1', '6', '8', '9']
        result = []
        helper(n, result, maps, "", keys)
        return result