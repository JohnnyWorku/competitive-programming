# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        shortest = float("inf")
        left = 0
        _sum = 0

        for right in range(len(nums)):
            _sum += nums[right]
            while _sum >= target:
                shortest = min(shortest, right - left + 1)
                _sum -= nums[left]
                left += 1

        return shortest if shortest != float("inf") else 0
