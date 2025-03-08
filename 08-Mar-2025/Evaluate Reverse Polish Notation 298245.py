# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == "+":
                operand_two = stack.pop()
                operand_one = stack.pop()
                result = operand_one + operand_two
                stack.append(result)
            elif char == "-":
                operand_two = stack.pop()
                operand_one = stack.pop()
                result = operand_one - operand_two
                stack.append(result)
            elif char == "*":
                operand_two = stack.pop()
                operand_one = stack.pop()
                result = operand_one * operand_two
                stack.append(result)
            elif char == "/": 
                operand_two = stack.pop()
                operand_one = stack.pop()
                result = int(int(operand_one / operand_two))
                stack.append(result)
            else:
                stack.append(int(char))
        return stack[0]