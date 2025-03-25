# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_position(arr, target, left, right):
            while left <= right:
                mid = left + ((right - left) // 2)

                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return left if left < len(arr) and arr[left] == target else -1

        def last_position(arr, target, left, right):
            while left <= right:
                mid = left + ((right - left) // 2)

                if arr[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return right if right >= 0 and arr[right] == target else -1

        # # one way
        # first, last = first_position(nums, target, 0, len(nums) - 1), last_position(nums, target, 0, len(nums) - 1)
        # return [first, last]
        # Another way
        first = first_position(nums, target, 0, len(nums) - 1)
        if first == -1:
            return [-1, -1]
        last = last_position(nums, target, 0, len(nums) - 1)
        
        return [first, last]
            