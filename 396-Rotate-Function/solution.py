class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        cur, n, temp = 0, len(A), 0
        for i in range(n):
            cur += A[i] * i
            temp += A[i]
        max_val = cur
        for i in range(1, n):
            cur -= A[n - i] * (n - 1)
            cur += temp - A[n - i]
            max_val = max(max_val, cur)
        return max_val