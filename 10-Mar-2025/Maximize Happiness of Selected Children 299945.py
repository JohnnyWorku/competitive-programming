# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        turns = 0
        selected_children_happiness = 0
        more_than_zero = True

        for i in range(len(happiness) - 1, -1, -1):
            if happiness[i] - turns < 0:
                more_than_zero = False

            if turns < k and more_than_zero:
                    selected_children_happiness += happiness[i] - turns
                    turns += 1

            if not more_than_zero or turns > k:
                break

        return selected_children_happiness
        