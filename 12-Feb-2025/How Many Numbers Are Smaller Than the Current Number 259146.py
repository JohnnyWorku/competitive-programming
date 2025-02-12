# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq_counter = [0] * (max(nums) + 1)
        for num in nums:
            freq_counter[num] += 1

        prefix_freq_counter = [freq_counter[0]]
        for i in range(1, len(freq_counter)):
            prefix_freq_counter.append(prefix_freq_counter[i - 1] + freq_counter[i])

        res = []
        for num in nums:
            if num == 0: # since 0 is the least no(based on constraint) it can't be greater than any no
                res.append(0)
            else:
                res.append(prefix_freq_counter[num - 1])

        return res
