import collections
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 0 or t < 0:
            return False
        window = collections.OrderedDict()
        for n in nums:
            if len(window) > k:
                window.popitem(False)
            bucket = n if not t else n // t
            for m in (window.get(bucket - 1), window.get(bucket), window.get(bucket + 1)):
                if m is not None and abs(n - m) <= t:
                    return True
            window[bucket] = n
        return False
        """
        if k < 0 or t < 0:
            return False
	    maps = collections.OrderedDict()
	    for i, num in enumerate(nums):
		    if len(maps) > k:
			    maps.popitem(False)
		    bucket = num if t == 0 else num / t
		    if val in (maps.get(bucket), maps.get(bucket - 1), maps.get(bucket + 1)):
			    if val and abs(val - num) <= t:
				    return True
		    maps[bucket] = num
	    return False
	    """