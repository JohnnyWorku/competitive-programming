# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # There will be two sections in this nums array
        # increasing from left to some point
        # increasing from some point to the end

        low, high = 0, len(nums) - 1
        res = float("inf")

        while low <= high:
            if nums[low] < nums[high]:
                res = min(res, nums[low])
                break
            
            mid = low + ((high - low) // 2)
            res = min(res, nums[mid])

            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1

        return res
        