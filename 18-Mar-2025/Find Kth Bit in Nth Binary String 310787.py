# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = 2 ** n - 1

        def helper(length, k):
            if length == 1:
                return "0"

            half = length // 2
            # if k is on the left side
            if k <= half:
                return helper(half, k)
            # if k is on the right side
            elif k > half + 1:
                res = helper(half, 1 + length - k)
                return "0" if res == "1" else "1"
            else:
                return "1"

        return helper(length, k)
        