# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        maximum = abs(nums[0])

        for num in nums:
            maximum = max(maximum, abs(num))

        min_negative = 0
        for num in nums:
            if num < 0:
                min_negative = min(min_negative, num)

        offset = abs(min_negative)

        freq_counter = [0] * (maximum + offset + 1)
        for num in nums:
            freq_counter[num + offset] += 1

        index = 0
        for i in range(len(freq_counter)):
            while freq_counter[i] > 0:
                nums[index] = i - offset
                index += 1
                freq_counter[i] -= 1

        return nums
        