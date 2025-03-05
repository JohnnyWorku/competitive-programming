# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key=lambda x: x[1])

        count = 0
        left = 0
        right = 1

        while right < len(sorted_points):
            if sorted_points[left][1] >= sorted_points[right][0]:
                right += 1
            else:
                count += 1
                left = right
                right += 1

        # To check the last groups or point
        if sorted_points[left][1] >= sorted_points[right - 1][0]:
            count += 1

        return count
        