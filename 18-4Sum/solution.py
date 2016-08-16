class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        maps = collections.defaultdict(list)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                cur = nums[i] + nums[j]
                maps[cur].append([i, j])
        result, temp = [], set()
        for twosum in maps:
            if target - twosum in maps:
                list1 = maps[twosum]
                list2 = maps[target - twosum]
                for x in list1:
                    for y in list2:
                        if x[1] < y[0]:
                            cand = [nums[i] for i in x + y]
                            if tuple(cand) not in temp:
                                result.append(cand)
                                temp.add(tuple(cand))
        return result