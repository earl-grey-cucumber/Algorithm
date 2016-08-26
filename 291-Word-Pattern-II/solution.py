class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        w2p, p2w = {}, {}
        return self.match(pattern, str, 0, 0, w2p, p2w)

    def match(self, pattern, str, i, j, w2p, p2w):
        if i == len(pattern) and j == len(str):
            return True
        elif i == len(pattern) or j == len(str):
            return False
        p = pattern[i]
        if p in p2w:
            w = p2w[p]
            if w == str[j:j+len(w)]:  # Match pattern.
                return self.match(pattern, str, i + 1, j + len(w), w2p, p2w)
            else:
                return False
        else:
            for k in xrange(j, len(str)):  # Try any possible word
                w = str[j:k+1]
                if w not in w2p:
                    # Build mapping. Space: O(n + c)
                    w2p[w], p2w[p] = p, w;
                    if self.match(pattern, str, i + 1, k + 1, w2p, p2w):
                        return True
                    w2p.pop(w), p2w.pop(p);
        return False