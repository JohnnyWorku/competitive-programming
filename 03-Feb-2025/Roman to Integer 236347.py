# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        rom_arab_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
        number = 0

        i = len(s) - 1
        while i >= 0:
            if i > 0 and rom_arab_dict[s[i - 1]] < rom_arab_dict[s[i]]:
                num = rom_arab_dict[s[i]] - rom_arab_dict[s[i - 1]]
                number += num
                i -= 2
            else:
                number += rom_arab_dict[s[i]]
                i -= 1

        return number
