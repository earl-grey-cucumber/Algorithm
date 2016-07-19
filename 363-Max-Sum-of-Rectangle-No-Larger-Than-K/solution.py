class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return 0
        M, N = len(matrix), len(matrix[0])
        m, n = max(M, N), min(M, N)
        ans = None
        for x in range(n):
            sums = [0] * m
            for y in range(x, n):
                num, slist = 0, []
                for z in range(m):
                    sums[z] += matrix[z][y] if M > N else matrix[y][z]
                    num += sums[z]
                    if num <= k:
                        ans = max(num, ans)
                   
                    index = bisect.bisect_left(slist, num - k)
                    if index != len(slist):
                        ans = max(ans, num - slist[index])
                    bisect.insort(slist, num)
        return ans or 0