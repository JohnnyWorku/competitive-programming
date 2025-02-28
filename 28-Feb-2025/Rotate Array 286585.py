# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # this is helper function that accepts array and the length you want to reverse as an argument
        def reversor(arr, initial_index, stopping_index):
            l, r = initial_index, stopping_index - 1
            
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
            return arr

        # The basic idea to do this question is revesrse the whole list and then reverse the list from 0 to k and from k to the length of the list
        # Sometimes k may be larger than the length of the list
        k = k % len(nums)

        reversor(nums, 0, len(nums))
        reversor(nums, 0, k)
        reversor(nums, k, len(nums))
        