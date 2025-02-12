# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        for i in range(len(arr) - 1, -1, -1):
            range_max_index = arr.index(max(arr[:i + 1]))
            if range_max_index != i:
                arr[:range_max_index + 1] = arr[:range_max_index + 1][::-1]
                flips.append(range_max_index + 1)

                arr[:i + 1] = arr[:i + 1][::-1]
                flips.append(i + 1)

        return flips
        