# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            if n == 0:
                return 1
            return n * factorial((n - 1))

        n = factorial(n)

        count = 0
        while n > 0:
            last_no = n % 10
            if last_no == 0:
                count += 1
            else:
                break
            n //= 10

        return count

        