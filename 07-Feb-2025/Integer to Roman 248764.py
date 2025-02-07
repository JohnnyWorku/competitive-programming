# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_arab_list = [
            (1, "I"), (4, "IV"), (5, "V"),
            (9, "IX"), (10, "X"), (40, "XL"),
            (50, "L"), (90, "XC"), (100, "C"),
            (400, "CD"), (500, "D"), (900, "CM"),
            (1000, "M")
        ]

        roman = ""
        for rom_arab in reversed(roman_arab_list):
            freq = num // rom_arab[0]
            roman += freq * rom_arab[1]

            num %= rom_arab[0]

        return roman
