# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def ninety_degree_rotator(matrix):
            rotated = []

            for col_no in range(len(matrix[0])):
                row = []
                for row_no in range(len(matrix) - 1, -1, -1):
                    entry = matrix[row_no][col_no]
                    row.append(entry)

                rotated.append(row)

            return rotated

        for _ in range(4):
            mat = ninety_degree_rotator(mat)

            if mat == target:
                return True

        return False

        