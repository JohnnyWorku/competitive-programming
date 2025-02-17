# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        p_sum = [nums[0]]
        for i in range(1, len(nums)):
            p_sum.append(p_sum[i - 1] + nums[i])
        print(p_sum)
        
        for i in range(len(p_sum)):
            if i == 0:
                left_sum, right_sum = 0, p_sum[-1] - p_sum[i]
            elif i == len(p_sum) - 1:
                left_sum, right_sum = p_sum[i - 1], 0
            else:
                left_sum, right_sum = p_sum[i - 1], p_sum[-1] - p_sum[i]

            if left_sum == right_sum:
                return i

        return -1
