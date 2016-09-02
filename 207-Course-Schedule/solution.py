class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        if not numCourses or not prerequisites:
            return True
        courses = [i for i in range(numCourses)]
        graph = {}
        for c in courses:
            graph[c] = []
        for pre in prerequisites:
            from_node, to_node = pre[1], pre[0]
            graph[from_node].append(to_node)
        visited, path = set(), []
        for c in courses:
            if not self.dfs(c, visited, path, graph):
                return False
        return len(visited) == len(graph)
    
    def dfs(self, c, visited, path, graph):
        if c in path:
            return False
        if len(visited) == len(graph):
            return True
        if c not in visited:
            visited.add(c)
            path.append(c)
            for node in graph[c]:
                if not self.dfs(node, visited, path, graph):
                    return False
            path.pop(-1)
        return True

        """
        if not numCourses or not prerequisites:
            return True
        courses = [i for i in range(numCourses)]
        graph, ins = {}, {}
        for c in courses:
            graph[c] = []
            ins[c] = 0 
        for pre in prerequisites:
            from_node, to_node = pre[1], pre[0]
            graph[from_node].append(to_node)
            ins[to_node] += 1
        queue, result = [], []
        for i in ins:
            if ins[i] == 0:
                queue.append(i)
                result.append(i)
        while queue:
            cur = queue.pop(0)
            for node in graph[cur]:
                ins[node] -= 1
                if ins[node] == 0:
                    queue.append(node)
                    result.append(node)
        return len(result) == len(graph)
        """