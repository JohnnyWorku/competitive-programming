# Problem: Largest Number - https://leetcode.com/problems/largest-number/

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