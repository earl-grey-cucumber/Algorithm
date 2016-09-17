class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        def helper_col1(image, i, j, top, bottom, opt):
            left = j
            while i <= j:
                k, mid = top, (i + j) / 2
                while k < bottom and image[k][mid] == '0':
                    k += 1
                if k < bottom:
                    left = min(left, mid)
                    j = mid - 1
                else:
                    i = mid + 1
            return left
        def helper_col2(image, i, j, top, bottom, opt):
            right = i
            while i <= j:
                k, mid = top, (i + j) / 2
                while k < bottom and image[k][mid] == '0':
                    k += 1
                if k < bottom:
                    right = max(right, mid)
                    i = mid + 1
                else:
                    j = mid - 1
            return right
            
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
        left = helper_col1(image, 0, y, 0, m, True)
        right = helper_col2(image, y, n - 1, 0, m, False)
        top = helper_row(image, 0, x, left, right + 1, True)
        bottom = helper_row(image, x + 1, m, left, right + 1, False)
        return (right - left + 1) * (bottom - top)
