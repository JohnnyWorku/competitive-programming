# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # Stack and greedy concept
        res, stack = [], []

        for i in range(len(pattern) + 1):
            stack.append(i + 1)

            while stack and (i == len(pattern) or pattern[i] == "I"):
                res.append(str(stack.pop()))

        return "".join(res)
        