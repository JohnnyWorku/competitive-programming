# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        counter_array = [0 for _ in range(max(nums) + 1)]

        for num in nums:
            counter_array[num] += 1

        for i in range(len(counter_array)):
            if i != len(counter_array) - 1 and counter_array[i] == 0:
                return i

        return len(counter_array)
