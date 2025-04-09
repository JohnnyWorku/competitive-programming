# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def fixed_car_counter(time):
            count = 0
            for rank in ranks:
                count += int(sqrt(time / rank))

            return count

        low, high = 1, ranks[0] * cars * cars
        res = 0
        while low <= high:
            mid = low + ((high - low) // 2)

            if fixed_car_counter(mid) >= cars:
                res = mid
                high = mid - 1

            else:
                low = mid + 1

        return res
        