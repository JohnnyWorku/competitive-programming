# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left = 0
        right = len(matrix[0]) - 1

        while left < right:
            # This is going upto right - 1
            for i in range(right - left):
                top = left
                bottom = right

                top_left = matrix[top][left + i]

                # moving bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # moving bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # moving top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # moving top left to top right
                matrix[top + i][right] = top_left

            right -= 1
            left += 1
        