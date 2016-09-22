from heapq import *
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [0] * n
        heap = []
        for i in range(len(primes)):
            heap.append([primes[i], 1, primes[i]])
        heapify(heap)
        ugly[0] = 1
        for i in range(1, n):
            ugly[i] = heap[0][0]
            while ugly[i] == heap[0][0]:
                cur = heappop(heap)
                heappush(heap, [cur[2] * ugly[cur[1]], cur[1] + 1, cur[2]])
        return ugly[n - 1]