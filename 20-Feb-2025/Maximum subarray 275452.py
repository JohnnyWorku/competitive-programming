# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = -float("inf")
        curr_total = 0

        for num in nums:
            curr_total += num
            total = max(curr_total, total)
            if curr_total < 0: # Its intution is keep it as it is if it is pos else make it 0
                curr_total = 0

        return total
        