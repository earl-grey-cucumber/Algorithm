class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        if not tickets:
            return []
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            graph[a] += b,
        path = []
        def visit(airport):
            while graph[airport]:
                visit(graph[airport].pop())
            path.append(airport)
        visit('JFK')
        return path[::-1]
# 通过图（无向图或有向图）中所有边且每边仅通过一次的通路称为欧拉通路