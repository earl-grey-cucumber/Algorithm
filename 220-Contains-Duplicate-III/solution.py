import collections
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 0 or t < 0:
            return False
        maps = collections.OrderedDict()
        for i, num in enumerate(nums):
            if len(maps) > k:
                maps.popitem(False)
            bucket = num if t == 0 else num // t
            for val in (maps.get(bucket), maps.get(bucket - 1), maps.get(bucket + 1)):
                if val is not None and abs(val - num) <= t:
                    return True
            maps[bucket] = num
        return False