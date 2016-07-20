class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 0 or t < 0:
            return False
        window = collections.OrderedDict()
        for num in nums:
            if len(window) > k:
                window.popitem(False)
            gap = num if not t else num // t
            for val in(window.get(gap - 1), window.get(gap), window.get(gap + 1)):
                if val is not None and abs(val - num) <= t:
                    return True
                window[gap] = num
        return False