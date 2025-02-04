# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # count = 0

        # for num in range(left, right + 1):
        #     for lst in ranges:
        #         if lst[0] <= num <= lst[-1]:
        #             pass
        #         else:
        #             count += 1

        #     if count == len(ranges):
        #         return False

        #     count = 0

        # return True

        check_set = {num for num in range(left, right + 1)}
        ranges_set = set()

        for _range in ranges:
            ranges_set.update({i for i in range(_range[0], _range[1] + 1)})

        for num in check_set:
            if num not in ranges_set:
                return False

        return True
