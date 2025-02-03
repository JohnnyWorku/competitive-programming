# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        ans = []
        for n in digits:
            num = num * 10 + n

        num += 1

        for number in str(num):
            ans.append(int(number))

        return ans