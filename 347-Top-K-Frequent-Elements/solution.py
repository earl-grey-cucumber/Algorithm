class Solution(object):
    def topKFrequent(self, nums, k):
        maps = {}
        max_f = 0
        for num in nums:
            if num not in maps:
                maps[num] = 0
            maps[num] += 1
            max_f = max(max_f, maps[num])
        bucket = [[] for i in range(max_f + 1)]
        for key in maps:
            f = maps[key]
            bucket[f].append(key)
        result = []
        i = max_f
        while i >= 0 and len(result) < k:
            result += bucket[i]
            i -= 1
        return result