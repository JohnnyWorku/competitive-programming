# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checker(rate, given_time):
            total_time = 0
            for pile in piles:
                total_time += ceil(pile / rate)

            return total_time <= given_time

        low, high = 1, max(piles)
        res = low

        while low <= high:
            mid = low + ((high - low) // 2)

            if checker(mid, h):
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res
        