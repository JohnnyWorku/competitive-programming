# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if all(num == 0 for num in nums):
            return 0

        def checker(arr, curr_prefix):
            for num, pref in zip(arr, curr_prefix):
                if num > pref:
                    return False
            return True

        low, high = 0, len(queries) - 1
        res = -1
        updated = False

        while low <= high:
            mid = low + ((high - low) // 2)

            prefix = [0] * (len(nums) + 1)
            for left, right, val in queries[:mid + 1]:
                prefix[left] += val
                prefix[right + 1] -= val

            for i in range(1, len(prefix)):
                prefix[i] += prefix[i - 1]

            if checker(nums, prefix):
                res = mid
                updated = True
                high = mid - 1
            else:
                low = mid + 1

        return res + 1 if updated else res
        