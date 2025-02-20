# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        # self.prefix_matrix = copy.deepcopy(self.matrix)

        # for row in range(len(self.matrix)):
        #     for col in range(1, len(self.matrix[0])):
        #         self.prefix_matrix[row][col] += self.prefix_matrix[row][col - 1]

        # for col in range(len(self.matrix[0])):
        #     for row in range(1, len(self.matrix)):
        #         self.prefix_matrix[row][col] += self.prefix_matrix[row - 1][col]

        self.prefix_matrix = [[0] * (len(self.matrix[0]) + 1) for row in range(len(self.matrix) + 1)]

        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                self.prefix_matrix[row + 1][col + 1] = self.prefix_matrix[row + 1][col] + self.prefix_matrix[row][col + 1] + self.matrix[row][col] - self.prefix_matrix[row][col]
 
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # if row1 == col1 == 0:
        #     range_sum = self.prefix_matrix[row2][col2]
        # elif row1 == 0:
        #     range_sum = self.prefix_matrix[row2][col2] - self.prefix_matrix[row2][col1 - 1]
        # elif col1 == 0:
        #     range_sum = self.prefix_matrix[row2][col2] - self.prefix_matrix[row1 - 1][col2]
        # else:
            # range_sum = self.prefix_matrix[row2][col2] - self.prefix_matrix[row1 - 1][col2] - self.prefix_matrix[row2][col1 - 1] + self.prefix_matrix[row1 - 1][col1 - 1]
        
        range_sum = self.prefix_matrix[row2 + 1][col2 + 1] - self.prefix_matrix[row1][col2 + 1] - self.prefix_matrix[row2 + 1][col1] + self.prefix_matrix[row1][col1]
        return range_sum
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)