# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # # Using the idea that if the current jumping num is >= distance
        # can_we = True
        # distance = 1

        # i = len(nums) - 2
        # while i > -1:
        #     if nums[i] < distance:
        #         can_we = False
        #     else:
        #         can_we = True
        #         distance = 1

        #     if not can_we:
        #         distance += 1

        #     i -= 1

        # return can_we

        # The greedier way
            goal = len(nums) - 1
            is_true = True
            
            i = len(nums) - 2
            while i >= 0:
                if i + nums[i] >= goal:
                    goal = i
                    is_true = True
                else:
                    is_true = False
                i -= 1

            return is_true
        
