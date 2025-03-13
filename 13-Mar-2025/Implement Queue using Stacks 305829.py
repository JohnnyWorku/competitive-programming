# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        if not self.output_stack:
            self.output_stack = self.input_stack[::-1]
            self.input_stack = []

        return self.output_stack.pop()

    def peek(self) -> int:
        if self.output_stack:
            return self.output_stack[-1]
        elif self.input_stack:
            return self.input_stack[0]

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()