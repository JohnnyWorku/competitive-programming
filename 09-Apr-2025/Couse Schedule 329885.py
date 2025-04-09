# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        white = 1
        gray = 2
        black = 3

        adj_list = defaultdict(list)

        for course in prerequisites:
            adj_list[course[1]].append(course[0]) 

        color = {k: white for k in range(numCourses)}
        no_cycle = True

        def dfs(node):
            nonlocal no_cycle

            if not no_cycle:
                return

            color[node] = gray

            for neighbour in adj_list[node]:
                if color[neighbour] == white:
                    dfs(neighbour)
                elif color[neighbour] == gray:
                    no_cycle = False

            color[node] = black

        for course in range(numCourses):
            if color[course] == white:
                dfs(course)

        return no_cycle
        