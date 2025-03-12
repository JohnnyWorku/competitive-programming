# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        closest = sum(nums[:3])
        min_range = abs(target- closest)

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                curr_range = target - curr_sum

                if curr_range == 0:  # When their range becomes zero
                    return target
                elif curr_range > 0:
                    if abs(curr_range) < min_range:
                        min_range = abs(curr_range)
                        closest = curr_sum
                    left += 1
                else:
                    if abs(curr_range) < min_range:
                        min_range = abs(curr_range)
                        closest = curr_sum
                    right -= 1

        return closest
