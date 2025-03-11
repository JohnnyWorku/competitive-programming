# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbit_counter = defaultdict(int)
        res = 0

        for answer in answers:
            rabbit_counter[str(answer)] += 1
            if rabbit_counter[str(answer)] == answer + 1:
                res += answer + 1
                del rabbit_counter[str(answer)]

        for key in rabbit_counter:
            res += int(key) + 1

        return res
        