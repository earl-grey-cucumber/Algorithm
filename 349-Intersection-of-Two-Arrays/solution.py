class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        temp1 = set(nums1)
        temp2 = set()
        for num in nums2:
            if num in temp1:
                temp2.add(num)
        return list(temp2)
