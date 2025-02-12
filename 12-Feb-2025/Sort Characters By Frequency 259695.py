# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        asci_store = []
        for letter in s:
            asci_store.append(ord(letter))

        asci_freq = [0] * (max(asci_store) + 1)
        for asci in asci_store:
            asci_freq[asci] += 1

        output_list = []
        for _ in range(len(asci_freq)):
            max_index = asci_freq.index(max(asci_freq))  # max_index is the ascii of the letter with max repititon
            while asci_freq[max_index] > 0:
                output_list.append(chr(max_index))
                asci_freq[max_index] -= 1

        return "".join(output_list)
