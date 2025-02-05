# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        keyboard_row = []

        row_letter = {
            1: "qwertyuiop",
            2: "asdfghjkl",
            3: "zxcvbnm"
        }

        for word in words:
            keyboard_row = []
            for letter in word:
                if letter.lower() in row_letter[1]:
                    keyboard_row.append(1)
                elif letter.lower() in row_letter[2]:
                    keyboard_row.append(2)
                else:
                    keyboard_row.append(3)
            print(keyboard_row)
            if len(set(keyboard_row)) == 1:
                ans.append(word)

        return ans
