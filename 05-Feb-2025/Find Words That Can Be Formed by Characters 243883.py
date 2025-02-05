# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counter = Counter(chars)
        total_counter = 0

        for word in words:
            letter_counter = 0
            word_counter = Counter(word)

            for key, value in word_counter.items():
                if key in chars_counter and value <= chars_counter[key]:
                    letter_counter += value

            if letter_counter == len(word):
                total_counter += len(word)

        return total_counter
                    