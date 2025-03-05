# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        tracker = defaultdict(int)
        count = 0

        for i in range(len(s)):
            tracker[s[i]] += 1
            if tracker["L"] == tracker["R"]:
                count += 1

        return count
