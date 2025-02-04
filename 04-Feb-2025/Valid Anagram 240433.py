# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        s_counter = Counter(s)
        t_counter = Counter(t)

        return True if s_counter == t_counter else False