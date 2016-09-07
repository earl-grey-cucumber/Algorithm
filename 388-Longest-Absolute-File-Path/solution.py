class Solution(object):
    def lengthLongestPath(self, input):
        maxlen = 0
        lines = input.splitlines()
        maps = {0: 0}
        for line in lines:
            content = line.lstrip('\t')
            depth = len(line) - len(content)
            if '.' in content:
                maxlen = max(maxlen, maps[depth] + len(content))
            else:
                maps[depth + 1] = maps[depth] + len(content) + 1
        return maxlen