# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []

        for col_no in range(len(matrix[0])):
            row = []
            for row_no in range(len(matrix)):
                row.append(matrix[row_no][col_no])
            transpose.append(row)

        return transpose
