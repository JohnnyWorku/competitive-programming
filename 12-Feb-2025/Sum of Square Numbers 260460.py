# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # use the idea that the sum of square of two nos become a number if the nos are less than square root of it
        left = 0
        right = int(sqrt(c))
        
        while left <= right:
            if (left ** 2) + (right ** 2) == c:
                return True
            elif (left ** 2) + (right ** 2) < c:
                left += 1
            else:
                right -= 1

        return False
        