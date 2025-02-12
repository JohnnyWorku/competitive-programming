# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        # the idea is after sorting piles giving the possible least coins to bob( be selfish somehow :) )
        freq_counter = [0] * (max(piles) + 1)
        for pile in piles:
            freq_counter[pile] += 1

        index = 0
        for i in range(len(freq_counter)):
            while freq_counter[i] > 0:
                piles[index] = i
                freq_counter[i] -= 1
                index += 1

        mine_pointer = len(piles) - 2
        bob_pointer = 0
        mine_counter = 0

        while bob_pointer < mine_pointer:
            mine_counter += piles[mine_pointer]
            mine_pointer -= 2
            bob_pointer += 1

        return mine_counter
        