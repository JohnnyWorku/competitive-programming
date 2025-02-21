# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_sum = float("inf")
        letter_index_dict = {}

        for index, s in enumerate(list1):
            letter_index_dict[s] = index

        output = []
        for i in range(len(list2)):
            if list2[i] in letter_index_dict:
                indice_sum = i + letter_index_dict[list2[i]]
                if indice_sum == min_sum:
                    output.append(list2[i])

                elif indice_sum < min_sum:
                    output = [list2[i]]
                    min_sum = indice_sum

        return output
