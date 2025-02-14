# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        fruits_dict = defaultdict(int)
        max_fruits = 0

        for right in range(len(fruits)):
            fruits_dict[fruits[right]] += 1

            while len(fruits_dict) > 2:
                fruits_dict[fruits[left]] -= 1
                if fruits_dict[fruits[left]] == 0:
                    del fruits_dict[fruits[left]]

                left += 1

            max_fruits = max(max_fruits, right - left + 1) 

        return max_fruits