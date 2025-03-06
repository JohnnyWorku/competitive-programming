# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mon_decreasing_stack = []
        next_greater_dict = {}

        for num in nums2:
            while mon_decreasing_stack and mon_decreasing_stack[-1] < num:
                next_greater_dict[mon_decreasing_stack[-1]] = num
                mon_decreasing_stack.pop()
            mon_decreasing_stack.append(num)

        ans = []
        for num in nums1:
            ans.append(next_greater_dict.get(num, -1))

        return ans
        