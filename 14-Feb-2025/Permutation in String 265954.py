# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            def is_valid():
                for key in s1_counter:
                    if s1_counter[key] > window[key]:
                        return False
                return True

            s1_counter = Counter(s1)
            window = defaultdict(int)
            left = 0

            for right in range(len(s2)):
                window[s2[right]] += 1

                while len(window) > len(s1_counter) or right - left + 1 > len(s1):
                    window[s2[left]] -= 1
                    if window[s2[left]] == 0:
                        del window[s2[left]]

                    left += 1

                if len(s1_counter) == len(window) and is_valid():
                    return True

            return False