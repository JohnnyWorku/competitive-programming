# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_validator = True
        cols_validator = True

        # to validate the rows
        for row_no in range(len(board)):
            seen = set()
            for col_no in range(len(board[0])):
                entry = board[row_no][col_no]
                if entry.isalnum():
                    if entry in seen:
                        rows_validator = False
                    else:
                        seen.add(entry)

            if rows_validator == False:
                return False

        # to validate the columns
        for col_no in range(len(board[0])):
            seen = set()
            for row_no in range(len(board)):
                entry = board[row_no][col_no]
                if entry.isalnum():
                    if entry in seen:
                        cols_validator = False
                    else:
                        seen.add(entry)

            if cols_validator == False:
                return False

        # to validate the 3 * 3 sections
        sections_validator = True
        left_limit = 0
        right_limit = 3
        top_limit = 0
        bottom_limit = 3

        while bottom_limit <= len(board):
            while right_limit <= len(board[0]):
                seen = set()
                for row_no in range(top_limit, bottom_limit):
                    for col_no in range(left_limit, right_limit):
                        entry = board[row_no][col_no]
                        if entry.isalnum():
                            if entry in seen:
                                sections_validator = False
                            else:
                                seen.add(entry)

                    if sections_validator == False:
                        return False

                left_limit = right_limit
                right_limit += 3

            top_limit = bottom_limit
            bottom_limit += 3
            left_limit = 0
            right_limit = 3
            
        return True
                    