# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        ans = []
        s = s.split()
        longest = max(s, key = len)

        for i in range(len(longest)):
            created_str = ""
            for index, current_str in enumerate(s):
                if i < len(current_str):
                    created_str += current_str[i]
                else:
                    created_str += " "

            created_str = created_str.rstrip()
            ans.append(created_str)

        return ans
