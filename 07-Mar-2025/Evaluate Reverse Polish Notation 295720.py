# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+":
                operand_two = stack.pop()
                operand_one = stack.pop()
                result = int(operand_one) + int(operand_two)
                stack.append(str(result))
            elif char == "-":
                operand_two = stack.pop()
                operand_one = stack.pop()
                result = int(operand_one) - int(operand_two)
                stack.append(str(result))
            elif char == "*":
                operand_two = stack.pop()
                operand_one = stack.pop()
                result = int(operand_one) * int(operand_two)
                stack.append(str(result))
            elif char == "/": 
                operand_two = stack.pop()
                operand_one = stack.pop()
                result = int(int(operand_one) / int(operand_two))
                stack.append(str(result))
            else:
                stack.append(char)
        return int(stack[0])
        