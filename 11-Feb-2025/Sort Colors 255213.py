# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq_count = []
        for _ in range(max(nums) + 1):
            freq_count.append(0)

        for num in nums:
            freq_count[num] += 1

        index = 0
        for i in range(len(freq_count)):
            while freq_count[i] > 0:
                nums[index] = i
                freq_count[i] -= 1
                index += 1

        return nums