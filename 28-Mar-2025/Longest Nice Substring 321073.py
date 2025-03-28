# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def divide(given_string):
            # Base case
            if len(given_string) <= 1:
                return ""

            given_string_set = set(given_string)
            for index, char in enumerate(given_string):
                opposite_case = char.swapcase()
                if opposite_case not in given_string_set:
                    left_str = divide(given_string[:index])
                    right_str = divide(given_string[index + 1:])

                    if len(left_str) >= len(right_str):
                        return left_str
                    return right_str

            return given_string

        return divide(s)
        