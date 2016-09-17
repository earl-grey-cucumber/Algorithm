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
                while k <= bottom and image[k][mid] == '0':
                    k += 1
                if k <= bottom:
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
            
        def helper_row(image, i, j, left, right, opt, cand):
            while i <= j:
                k, mid = left, (i + j) / 2
                while k <= right and image[mid][k] == '0':
                    k += 1
                if k <= right:
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
        m, n = len(image), len(image[0])
        left = helper_col(image, 0, y, 0, m - 1, True, y)
        right = helper_col(image, y, n - 1, 0, m - 1, False, y)
        top = helper_row(image, 0, x, left, right, True, x)
        bottom = helper_row(image, x, m - 1, left, right, False, x)
        return (right - left + 1) * (bottom - top + 1)
