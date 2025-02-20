# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # with o(n) space using 1D prefix product
        # prefix = [1] * len(nums)
        # postfix = [1] * len(nums)

        # for i in range(1, len(nums)):
        #     prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # for i in range(len(nums) - 2, -1, -1):
        #     postfix[i] = postfix[i + 1] * nums[i + 1]

        # res = []
        # for pre, post in zip(prefix, postfix):
        #     res.append(pre * post)

        # return res

        # with o(1) space using running products
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

