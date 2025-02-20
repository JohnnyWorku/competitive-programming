# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_freq = defaultdict(int)
        prefix_freq[0] += 1 #Before the very start of the list their prefix is 0 as the exclusive

        ans = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            ans += prefix_freq[diff]
            prefix_freq[curr_sum] += 1

        return ans
