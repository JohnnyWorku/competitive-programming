# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1
        required_row = 0

        while low <= high:
            mid = low + ((high - low) // 2)

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                required_row = mid
                break

            elif matrix[mid][0] > target:
                high = mid - 1
            
            elif matrix[mid][-1] < target:
                low = mid + 1

        if low <= high: # If there is a range that contains target (the above loop breaked not ended)
            left, right = 0, len(matrix[required_row])

            while left <= right:
                mid = left + ((right - left) // 2)

                if matrix[required_row][mid] == target:
                    return True

                elif matrix[required_row][mid] > target:
                    right = mid - 1

                else:
                    left = mid + 1

        return False
        