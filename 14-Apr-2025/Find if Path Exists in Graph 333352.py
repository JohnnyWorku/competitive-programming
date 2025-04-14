# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for edge in edges:
            node1, node2 = edge
            graph[node1].append(node2)
            graph[node2].append(node1)

        ## Recursively

        # def dfs(node, visited):
        #     if node == destination:
        #         return True

        #     visited.add(node)

        #     for neighbour in graph[node]:
        #         if neighbour not in visited:
        #             found = dfs(neighbour, visited)
        #             if found:
        #                 return True

        #     return False

        # return dfs(source, set()) 

        ## Iteratively
        stack = [source]
        visited = set([source])

        while stack:
            node = stack.pop()
            if node == destination:
                return True

            for neighbour in graph[node]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    visited.add(neighbour)

        return False
        