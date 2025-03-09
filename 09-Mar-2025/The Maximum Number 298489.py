# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        arr = []

        for i in range(len(nums) - 1, -1, -1):
            if not arr:
                arr.append(nums[i])
            elif nums[i] != arr[-1]:
                arr.append(nums[i])

            if len(arr) == 3:
                return arr[-1]
        
        return arr[0] #If there are no three distinct nos in nums return the max
            

        
        