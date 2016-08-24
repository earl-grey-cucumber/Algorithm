class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        cur = 1
        for i in range(1, n + 1):
            result.append(cur)
            if cur * 10 <= n:
                cur *= 10
            elif cur % 10 != 9 and cur + 1 <= n:
                cur += 1
            else:
                while (cur / 10) % 10 == 9:
                    cur = cur / 10
                cur = cur / 10 + 1
        return result
        """
        top = 1
        while top * 10 <= n:
            top *= 10
        def mycmp(a, b, top=top):
            while a < top: a *= 10
            while b < top: b *= 10
            return -1 if a < b else b < a
        return sorted(xrange(1, n+1), mycmp)
        """
        """
        if n < 1: return []
        res = []
        for first in xrange(1, 10):
            if first > n: break
            res.append(first)
            self.get_all_number(first,n,res)
        return res
 
    def get_all_number(self, first, n, res):
        for i in xrange(10):
            t = first * 10 + i
            if t <= n:
                res.append(t)
                self.get_all_number(t, n, res)
            else:
                break
        """
        """
        if n < 1:
            return []
            
        def dfs(n, result, cur):
            if cur > n:
                return 
            if cur > 0:
                result.append(cur)                    
            for i in range(10):
                if i == 0 and cur == 0:
                   continue
                val = cur * 10 + i
                if val > n:
                    break
                dfs(n, result, val)
                       
        result = []
        dfs(n, result, 0)
        return result
        """