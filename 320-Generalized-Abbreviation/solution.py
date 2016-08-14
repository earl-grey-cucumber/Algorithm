class Solution(object):
    def generateAbbreviations(self, word):
        if len(word) == 0:
            return [""]
        def dfs(word, result, path, count, index):
            old_len = len(path)
            if index == len(word):
                if count > 0:
                    path += str(count)
                result.append(path)
            else:
                dfs(word, result, path, count + 1, index + 1)
                if count > 0:
                    path += str(count) 
                path += word[index]
                dfs(word, result, path, 0, index + 1)
            path = path[0: old_len]
        result = []
        dfs(word, result, "", 0, 0)
        return result
