# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc_queue = deque() # To track the minimum of the subarray
        dec_queue = deque() # To track the maximum of the subarray
        max_len = 0

        left = 0
        for right in range(len(nums)):
            while inc_queue and inc_queue[-1] > nums[right]:
                inc_queue.pop()

            inc_queue.append(nums[right])

            while dec_queue and dec_queue[-1] < nums[right]:
                dec_queue.pop()

            dec_queue.append(nums[right])

            while (inc_queue and dec_queue) and (dec_queue[0] - inc_queue[0] > limit):
                if inc_queue[0] == nums[left]:
                    inc_queue.popleft()
                if dec_queue[0] == nums[left]:
                    dec_queue.popleft()

                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
