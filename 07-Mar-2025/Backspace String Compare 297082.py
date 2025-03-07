# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        for char_s in s:
            if stack_s and char_s == "#":
                stack_s.pop()
            elif char_s.isalnum():
                stack_s.append(char_s)

        for char_t in t:
            if stack_t and char_t == "#":
                stack_t.pop()
            elif char_t.isalnum():
                stack_t.append(char_t)

        return "".join(stack_s) == "".join(stack_t)
