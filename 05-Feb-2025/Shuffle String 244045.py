# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        string_list = []

        for _ in range(len(s)):
            string_list.append(" ")

        for _s, index in zip(s, indices):
            string_list[index] = _s

        return "".join(string_list)
