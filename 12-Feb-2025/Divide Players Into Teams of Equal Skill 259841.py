# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) - 1

        chemistry_sum = 0
        are_equal = True
        skill_sum = skill[left] + skill[right]

        while left < right:
            if skill[left] + skill[right] != skill_sum:
                are_equal = False

            if are_equal == False:
                return -1

            else:
                chemistry_sum += skill[left] * skill[right]

            left += 1
            right -= 1

        return chemistry_sum
