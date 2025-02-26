# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        not_comments = []
        in_block = False

        for line in source:
            i = 0
            if not in_block:
                not_comments = []

            while i < len(line):
                if not in_block and line[i] == "/" and i + 1 < len(line) and line[i + 1] == "/":
                    break
                elif not in_block and line[i] == "/" and i + 1 < len(line) and line[i + 1] == "*":
                    in_block = True
                    i += 1  # since the next char is "*" skip it. This also holds the "/*/" case
                elif in_block and line[i] == "*" and i + 1 < len(line) and line[i + 1] == "/":
                    in_block = False
                    i += 1
                elif not in_block:
                    not_comments.append(line[i])
                i += 1

            if not_comments and not in_block:
                res.append("".join(not_comments))

        return res
