# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seeker = 0
        holder = 0

        for seeker in range(len(nums)):
            if nums[seeker] != 0:
                nums[seeker], nums[holder] = nums[holder], nums[seeker]

            if nums[holder] != 0:
                holder += 1
