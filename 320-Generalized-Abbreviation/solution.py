class Solution(object):
    def generateAbbreviations(self, word):
        """
        if len(word) == 0:
            return [""]
        def dfs(word, result, path, count, index):
            temp = path
            if index == len(word):
                if count:
                    path += str(count)
                result.append(path)
            else:
                dfs(word, result, path, count + 1, index + 1)
                if count:
                    path += str(count) 
                path += word[index]
                dfs(word, result, path, count, index + 1)
            path = temp
            
        result = []
        dfs(word, result, "", 0, 0)
        return result
        """
        result = []
        if len(word) == 0:
            return [""]
        self.helper(word, result, "", 0, 0)
        return result
    
    def helper(self, word, result, sb, index, count):
        old = len(sb)
        if index == len(word):
            if count > 0:
                sb += str(count)
            result.append(sb)
        else:
            self.helper(word, result, sb, index + 1, count + 1) # abr
            
            if count > 0:
                sb += str(count)
            sb += word[index] #3d, count comes befor char
            self.helper(word, result, sb, index + 1, 0) #no abr
        sb = sb[0:old]
