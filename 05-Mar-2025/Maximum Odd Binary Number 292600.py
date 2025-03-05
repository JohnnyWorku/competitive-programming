# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # # The idea is to make it odd one 1 must be at last position b/c it is the only position to make it odd

        # output = ["0"] * len(s)
        # one_counter = 0
        # check_last_position = False
        # for i in range(len(s)):
        #     if s[i] == "1" and not check_last_position:
        #         output[-1] = "1"
        #         check_last_position = True
        #     elif s[i] == "1" and check_last_position:
        #         one_counter += 1

        # place_holder = 0
        # while one_counter:
        #     output[place_holder] = "1"
        #     place_holder += 1
        #     one_counter -= 1

        # return "".join(output)

        # Another implementation seeker and place holder style and change the last one with the last zero to make it odd
        s = [letter for letter in s]
        left = 0

        for i in range(len(s)):
            if s[i] == "1":
                s[i], s[left] = s[left], s[i]
                left += 1

        s[left - 1], s[i] = s[i], s[left - 1]

        return "".join(s)
        