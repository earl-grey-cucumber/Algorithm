class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points:
            return True
        l, r = points[0][0], points[0][0]
        maps = {}
        for point in points:
            l = min(l, point[0])
            r = max(r, point[0])
            if point[0] not in maps:
                maps[point[0]] = set()
            maps[point[0]].add(point[1])
        mid = l + (r - l) / 2.0
        for i, point in enumerate(points):
            x, y = point[0], point[1]
            reflect_x = mid * 2 - x
            if reflect_x not in maps:
                return False
            if y not in maps[reflect_x]:
                return False
        return True