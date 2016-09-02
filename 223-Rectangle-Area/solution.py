class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        area = (C - A) * (D - B) + (G - E) * (H - F)
        if B>=H or F>=D or A>=G or E>=C:
            return area
        dup = (min(G, C) - max(E, A)) * (min(D, H) - max(B, F))
        return area - dup
        