class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ra, ca = len(A), len(A[0])
        rb, cb = len(B), len(B[0])
        mapa, mapb = {}, {}
        result = [[0 for i in range(cb)] for j in range(ra)]
        for i in range(ra):
            mapar = {}
            for j in range(ca):
                if A[i][j] != 0:
                    mapar[j] = A[i][j]
            if len(mapar) > 0:
                mapa[i] = mapar
        for i in range(cb):
            mapbc = {}
            for j in range(rb):
                if B[j][i] != 0:
                    mapbc[j] = B[j][i]
            if len(mapbc) > 0:
                mapb[i] = mapbc
        for i in range(ra):
            if i in mapa:
                for j in range(cb):
                    if j in mapb:
                        val = 0
                        for k in range(ca):
                            if k in mapa[i] and k in mapb[j]:
                                val += mapa[i][k] * mapb[j][k]
                        result[i][j] = val
        return result

                