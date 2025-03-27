# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def checker(capacity, day_no):
            curr_total = 0
            no_day = 0

            for weight in weights:
                curr_total += weight
                if curr_total > capacity or curr_total == capacity:
                    if curr_total > capacity:
                        curr_total = weight
                    else:
                        curr_total = 0

                    no_day += 1

            if curr_total:
                no_day += 1

            return no_day <= day_no

        low, high = max(weights), sum(weights)
        res = high

        while low <= high:
            middle = low + ((high - low) // 2)

            if checker(middle, days):
                res = middle
                high = middle - 1
            else:
                low = middle + 1

        return res
        