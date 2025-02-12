# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        freq_counter = [0] * (max(costs) + 1)

        for cost in costs:
            freq_counter[cost] += 1

        ice_cream_no = 0
        for cost, freq in enumerate(freq_counter):
            if coins >= cost:
                while coins >= cost and freq > 0: #to check if coins is still greater than cost(index) after buying
                    ice_cream_no += 1
                    coins -= cost
                    freq -= 1
            else:
                break

        return ice_cream_no
