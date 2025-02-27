# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_counter = defaultdict(int)

        for num in nums:
            num_counter[num] += 1
            if len(num_counter) > 2:
                new_counter = defaultdict(int)
                for key, value in num_counter.items():
                    if value > 1:
                        new_counter[key] = value - 1
                num_counter = new_counter
                    
        res = []
        for num in num_counter:
            if nums.count(num) > len(nums) // 3:
                res.append(num)

        return res
