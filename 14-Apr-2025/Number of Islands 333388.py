# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        total_islands = 0
        def dfs(row, col):
            visited[row][col] = True
            for hor, ver in directions:
                new_row = row + hor
                new_col = col + ver

                if inbound(new_row, new_col) and not visited[new_row][new_col] and grid[row][col] == "1":
                    dfs(new_row, new_col)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j)
                    total_islands += 1

        return total_islands
        