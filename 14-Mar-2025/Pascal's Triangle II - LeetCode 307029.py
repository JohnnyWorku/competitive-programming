# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            prev_arr = self.getRow(rowIndex - 1)

            res = [1] * (rowIndex + 1)
            left = 0
            right = 1
            position = 1
            while right < len(prev_arr):
                if position < len(res) - 1:
                    res[position] = prev_arr[left] + prev_arr[right]
                    left += 1
                    right += 1
                    position += 1
                else:
                    break

            return res
