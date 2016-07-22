class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if not points or len(points) < 2:
            return True
        minx, maxx = points[0][0], points[0][0]
        maps = {}
        maps[points[0][0]] = [points[0][1]]
        for i in range(1, len(points)):
            x, y = points[i][0], points[i][1]
            minx, maxx = min(minx, x), max(maxx, x)
            if x not in maps:
                maps[x] = [y]
            else:
                maps[x].append(y) 
        center_y = (minx + maxx) / 2.0

        for p in points:
            ref_x = 2 * center_y - p[0]
            if not (ref_x in maps and p[1] in maps[ref_x]):
                return False
        return True