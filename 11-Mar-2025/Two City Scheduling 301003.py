# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # The idea is to have a - b and decide to which city send that person keeping minimum cost
        
        diffs = []

        for cost_a, cost_b in costs:
            diff = cost_a - cost_b
            diffs.append((diff, cost_a, cost_b))

        diffs.sort()
        min_cost = 0
        for i in range(len(diffs)):
            if i < len(diffs) // 2: # Up to half or n / 2
                min_cost += diffs[i][1]
            else:
                min_cost += diffs[i][2]

        return min_cost
        