# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
            if len(firstList) == 0 or len(secondList) == 0:
                return []

            first_pointer = 0
            second_pointer = 0
            res = []

            while first_pointer < len(firstList) and second_pointer < len(secondList):
                start1, end1 = firstList[first_pointer]
                start2, end2 = secondList[second_pointer]

                if start1 > end2:
                    second_pointer += 1
                elif start2 > end1:
                    first_pointer += 1
                else:
                    res.append([max(start1, start2), min(end1, end2)])
                    if end1 > end2:
                        second_pointer += 1
                    else:
                        first_pointer += 1

            return res


        