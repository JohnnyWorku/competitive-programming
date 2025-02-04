# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for index, num in enumerate(nums):
            if (target - num) in nums_dict:
                return [nums_dict[target - num], index]
            else:
                nums_dict[num] = index
        
        return []
