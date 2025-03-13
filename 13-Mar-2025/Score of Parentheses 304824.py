# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for bracket in s:
            if bracket == "(":
                stack.append(0)
            else:
                last_score = stack.pop()
                stack[-1] += max(2 * last_score, 1)

        return stack[0]
        