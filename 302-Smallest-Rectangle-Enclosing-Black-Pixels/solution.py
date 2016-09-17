class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        def helper_col(image, i, j, top, bottom, opt):
            while i != j:
                k, mid = top, (i + j) / 2
                while k < bottom and image[k][mid] == '0':
                    k += 1
                if (k < bottom) == opt:
                    j = mid
                else:
                    i = mid + 1
            return i
        def helper_row(image, i, j, left, right, opt):
            while i != j:
                k, mid = left, (i + j) / 2
                while k < right and image[mid][k] == '0':
                    k += 1
                if (k < right) == opt:
                    j = mid
                else:
                    i = mid + 1
            return i
        m, n = len(image), len(image[0])
        left = helper_col(image, 0, y, 0, m, True)
        right = helper_col(image, y + 1, n, 0, m, False)
        top = helper_row(image, 0, x, left, right, True)
        bottom = helper_row(image, x + 1, m, left, right, False)
        return (right - left) * (bottom - top)
