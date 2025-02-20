# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_dict = defaultdict(int)
        remainder_dict[0] += 1

        res = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            remainder = curr_sum % k
            res += remainder_dict[remainder]
            remainder_dict[remainder] += 1

        return res
        