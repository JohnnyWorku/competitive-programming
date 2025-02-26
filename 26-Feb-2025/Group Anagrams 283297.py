# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            letter_count = Counter(word)
            letter_count = dict(sorted(letter_count.items()))
            groups[tuple(letter_count.items())].append(word)
            
        res = []
        for value in groups.values():
            res.append(value)

        return res
                