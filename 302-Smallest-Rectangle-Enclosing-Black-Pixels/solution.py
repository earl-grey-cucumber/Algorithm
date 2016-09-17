class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        def helper_col(image, i, j, top, bottom, opt, cand):
            while i <= j:
                k, mid = top, (i + j) / 2
                while k < bottom and image[k][mid] == '0':
                    k += 1
                if k < bottom:
                    if opt:
                        cand = min(cand, mid)
                        j = mid - 1
                    else:
                        cand = max(cand, mid)
                        i = mid + 1
                else:
                    if opt:
                        i = mid + 1
                    else:
                         j = mid - 1
            return cand
            
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
        left = helper_col(image, 0, y, 0, m, True, y)
        right = helper_col(image, y, n - 1, 0, m, False, y)
        top = helper_row(image, 0, x, left, right + 1, True)
        bottom = helper_row(image, x + 1, m, left, right + 1, False)
        return (right - left + 1) * (bottom - top)
