# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []

        def backtrack(output=[], length=n):
            if len(output) == n:
                res.append("".join(output[:]))
                return

            if not output or (output and output[-1] != "0"):
                output.append("0")
                backtrack(output, length)
                output.pop()

            output.append("1")
            backtrack(output, length)
            output.pop()

        backtrack()
        return res
