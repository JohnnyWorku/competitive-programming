# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indices = []
        freq_counter = [0] * (max(nums) + 1)

        for num in nums:
            freq_counter[num] += 1

        index = 0
        for i in range(len(freq_counter)):
            while freq_counter[i] > 0:
                nums[index] = i
                freq_counter[i] -= 1
                index += 1

        for i in range(len(nums)):
            if nums[i] == target:
                indices.append(i)

        return indices
