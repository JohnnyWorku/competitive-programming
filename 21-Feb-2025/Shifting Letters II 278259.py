# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        p_sum_list = [0] * (len(s) + 1)

        for shift in shifts:
            if shift[2] == 0:
                p_sum_list[shift[0]] -= 1
                p_sum_list[shift[1] + 1] += 1
            else:
                p_sum_list[shift[0]] += shift[2]
                p_sum_list[shift[1] + 1] -= shift[2]

        for i in range(1, len(p_sum_list)):
            p_sum_list[i] = p_sum_list[i - 1] + p_sum_list[i]

        print(p_sum_list)

        s_list = list(s)

        for i in range(len(s_list)):
            offset = ord('a')
            num = ord(s_list[i]) - offset
            num += p_sum_list[i] 
            num %= 26
            char = chr(num + offset)

            s_list[i] = char

        return "".join(s_list)
                        