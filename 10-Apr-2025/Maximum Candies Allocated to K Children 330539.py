# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def kids_counter(amount):
            count = 0
            
            if amount != 0:
                for pile in candies:
                    factor = int(pile / amount)
                    count += factor
            return count

        low, high = 1, sum(candies)
        res = 0

        while low <= high:
            mid = low + ((high - low) // 2)

            if kids_counter(mid) >= k:
                res = mid
                low = mid + 1
            else:
                high = mid - 1

        return res
        