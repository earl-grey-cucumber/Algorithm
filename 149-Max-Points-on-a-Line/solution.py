# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        result = 0
        for i in range(len(points)):
            maps = {float("-inf"): 1}
            same = 0
            for j in range(i + 1, len(points)):
                if points[j].x == points[i].x and points[j].y == points[i].y:
                    same += 1
                else:
                    if points[j].x == points[i].x:
                        key = float("inf")
                    else:
                        key = (float)(points[j].y - points[i].y) / (points[j].x - points[i].x)
                    if key not in maps:
                        maps[key] = 2
                    else:
                        maps[key] += 1
            for k in maps:
                result = max(result, maps[k] + same)
        return result