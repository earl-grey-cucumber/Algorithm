class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        n, k = len(costs), len(costs[0])
        if k == 1:
            return costs[0][0]
        pre_min, pre_sec_min, pre_min_index = 0, 0, -1
        for i in range(n):
            cur_min, cur_sec_min, cur_min_index = sys.maxint, sys.maxint, -1
            for j in range(k):
                if j == pre_min_index:
                    val = costs[i][j] + pre_sec_min
                else:
                    val = costs[i][j] + pre_min
                if val < cur_min:
                    cur_sec_min = cur_min
                    cur_min = val
                    cur_min_index = j
                elif val < cur_sec_min:
                    cur_sec_min = val
            pre_min = cur_min
            pre_sec_min = cur_sec_min
            pre_min_index = cur_min_index
        return pre_min