# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # sorting them with cyclic sort
        i = 0
        while i < len(nums):
            if nums[i] == i + 1:
                i += 1
            else:
                temp_index = nums[i] - 1
                if nums[i] != nums[temp_index]:
                    nums[temp_index], nums[i] = nums[i], nums[temp_index]
                else:
                    i += 1

        # traversing over the list to obtain the duplicates
        ans = []
        for j in range(len(nums)):
            if nums[j] != j + 1:
                ans.append(nums[j])

        return ans
