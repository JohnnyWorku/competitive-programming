# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ## Informal way
        # count = 0
        # for row in range(len(grid)):
        #     for col in range(len(grid[0])):
        #         count += 1 if grid[row][col] == 1 else 0

        # return (count + 1) * 2

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = [[False for col in range(len(grid[0]))] for row in range(len(grid))]

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        parameter = 0
        def dfs(grid, visited, row, col):
            nonlocal parameter

            visited[row][col] = True

            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change

                if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                    if not visited[new_row][new_col]:
                        dfs(grid, visited, new_row, new_col)

                else:
                    parameter += 1

        # Trying to find the first land
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(grid, visited, row, col)
                    return parameter

        return 0
        