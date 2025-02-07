# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top_limit = 0
        bottom_limit = len(matrix) - 1
        left_limit = 0
        right_limit = len(matrix[0]) - 1
        spiral_order_list = []

        while top_limit <= bottom_limit and left_limit <= right_limit:
            # going from left to right
            for column_pointer in range(left_limit, right_limit + 1):
                spiral_order_list.append(matrix[top_limit][column_pointer])

            top_limit += 1

            # going from top to bottom
            for row_pointer in range(top_limit, bottom_limit + 1):
                spiral_order_list.append(matrix[row_pointer][right_limit])

            right_limit -= 1

            if top_limit <= bottom_limit:
                # going from right to left
                for column_pointer in range(right_limit, left_limit - 1, -1):
                    spiral_order_list.append(matrix[bottom_limit][column_pointer])

                bottom_limit -= 1

            if left_limit <= right_limit:
                # going from bottom to top
                for row_pointer in range(bottom_limit, top_limit - 1, -1):
                    spiral_order_list.append(matrix[row_pointer][left_limit])

                left_limit += 1

        return spiral_order_list
        