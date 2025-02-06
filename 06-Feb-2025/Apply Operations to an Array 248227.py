# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        print(nums)
        place_holder = 0
        seeker = 0

        while place_holder <= seeker < len(nums):
            if nums[seeker] != 0 and nums[place_holder] == 0:
                nums[seeker], nums[place_holder] = nums[place_holder], nums[seeker]
                place_holder += 1

            elif nums[seeker] != 0 and nums[place_holder] != 0:
                place_holder += 1

            seeker += 1

        return nums

