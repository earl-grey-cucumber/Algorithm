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
        if not points or len(points) < 1:
            return 0
        max_count, n = 1, len(points)
        for i in range(n):
            same = 0
            mapping = {float("-inf"): 1}
            for j in range(i + 1, n):
                key = 0.0
                if points[j].x == points[i].x and points[j].y == points[i].y:
                    same += 1
                else:
                    if points[j].x == points[i].x:
                        key = float("inf")
                    else:
                        key = (0.0 + points[i].y-points[j].y)/(points[i].x-points[j].x)
                    if key not in mapping:
                        mapping[key] = 2
                    else:
                        mapping[key] += 1
                for val in mapping.values():
                    max_count = max(max_count, val + same)
        return max_count