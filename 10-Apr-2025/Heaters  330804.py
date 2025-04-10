# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def checker(radius, houses, heaters):
            i, j = 0, 0
            while j < len(heaters):
                max_zone = heaters[j] + radius
                min_zone = heaters[j] - radius

                while i < len(houses) and min_zone <= houses[i] <= max_zone:
                    i += 1

                if i == len(houses):
                    return True

                j += 1
            return False

        low, high = 0, max(houses[-1], heaters[-1])
        res = 0

        while low <= high:
            mid = (low + high) // 2

            if checker(mid, houses, heaters):
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res
        