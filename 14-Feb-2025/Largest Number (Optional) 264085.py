# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # result = ""
        # for i in range(len(nums)):
        #     for j in range(len(nums) - i - 1):
        #         if f"{nums[j]}{nums[j + 1]}" > f"{nums[j + 1]}{nums[j]}":
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        # nums.reverse()
        
        # for num in nums:
        #     result += str(num)

        # i = 0
        # if len(result) > 1:
        #     while i < len(result) and result[i] == "0":
        #         i += 1
        # result = result[i:]


        # return "0" if len(result) == 0 else result










        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if f"{nums[j]}{nums[j + 1]}" > f"{nums[j + 1]}{nums[j]}":
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        result = "".join(list(map(str, nums[::-1])))

        i = 0
        if len(nums) > 1:
            while i < len(nums) and result[i] == "0":
                i += 1

        result = result[i:]

        return "0" if len(result) == 0 else result
