# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        s_list = list(s)

        holder = 0
        counter = 0

        for seeker in range(len(s)):
            if s_list[seeker] == "0":
                s_list[seeker], s_list[holder] = s_list[holder], s_list[seeker]
                counter += seeker - holder

                holder += 1

        return counter
    