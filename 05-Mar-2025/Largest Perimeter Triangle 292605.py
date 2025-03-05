# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # The idea is to determine it is a valid tringle the largest side must be less than the sum of the other sides
        nums.sort()
        i = len(nums) - 1
        perimeter = 0
        while i >= 2:
            if nums[i - 2] + nums[i - 1] > nums[i]:
                perimeter = nums[i - 2] + nums[i - 1] + nums[i]
                break
            i -= 1

        return perimeter
        