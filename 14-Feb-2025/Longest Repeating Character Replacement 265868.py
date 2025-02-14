# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alpha_dict = defaultdict(int)
        left = 0
        longest = 0

        for right in range(len(s)):
            alpha_dict[s[right]] += 1
            max_freq = max(alpha_dict.values())

            while (right - left + 1) - max_freq > k:
                alpha_dict[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest
