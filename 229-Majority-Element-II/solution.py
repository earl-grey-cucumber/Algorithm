class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        maps = {}
        k = 3
        for num in nums:
            if num in maps:
                maps[num] += 1
            elif len(maps) < k:
                maps[num] = 1
            if len(maps) == k:
                for key in maps.keys():
                    maps[key] -= 1
                    if maps[key] == 0:
                        del maps[key]
        result = []
        for key in maps:
            maps[key] = 0
        for num in nums:
            if num in maps:
                maps[num] += 1
        for key in maps:
            if maps[key] * 3 > len(nums):
                result.append(key)
        return result
                    