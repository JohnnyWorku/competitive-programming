# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter = Counter(p)
        s_counter = defaultdict(int)
        left = 0
        indices_store = []

        for right in range(len(s)):
            s_counter[s[right]] += 1

            if s_counter == p_counter:
                indices_store.append(left)

                s_counter[s[left]] -= 1
                if s_counter[s[left]] == 0:
                    del s_counter[s[left]]
                left += 1

            elif s_counter != p_counter and right - left + 1 == len(p):
                s_counter[s[left]] -= 1
                if s_counter[s[left]] == 0:
                    del s_counter[s[left]]
                left += 1

        return indices_store
        
