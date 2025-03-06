# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        mon_decreasing_stack = []
        for index, temp in enumerate(temperatures):
            while mon_decreasing_stack and mon_decreasing_stack[-1][0] < temp:
                res[mon_decreasing_stack[-1][1]] = index - mon_decreasing_stack[-1][1]
                mon_decreasing_stack.pop()
            mon_decreasing_stack.append((temp, index))

        return res
