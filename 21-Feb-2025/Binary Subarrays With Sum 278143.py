# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Using running sum and dictionary
        nums_dict = defaultdict(int)
        nums_dict[0] += 1
        
        curr_sum = 0
        sub_arrays = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            diff = curr_sum - goal

            if diff in nums_dict:
                sub_arrays += nums_dict[diff]

            nums_dict[curr_sum] += 1

        return sub_arrays
        