# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        turns = rows + cols - 1
        turns_store = [[] for _ in range(turns)]
        diagonal_order_list = []

        for row in range(rows):
            for col in range(cols):
                turns_store[row + col].append(mat[row][col])

        for turn in range(len(turns_store)):
            if turn % 2 == 0:
                diagonal_order_list.extend(turns_store[turn][::-1])
            else:
                diagonal_order_list.extend(turns_store[turn])


        return diagonal_order_list
