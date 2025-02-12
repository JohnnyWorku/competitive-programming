# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        moves = 0
        for seat, student in zip(seats, students):
            moves += abs(seat - student)

        return moves
        