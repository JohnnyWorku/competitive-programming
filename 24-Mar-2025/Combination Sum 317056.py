# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def combinations(arr, total, index=0, sequence=[], curr_sum=0):
            if curr_sum > total:
                return
            if index == len(arr):
                if curr_sum == total:
                    res.append(sequence[:])
                return

            sequence.append(arr[index])
            curr_sum += arr[index]
            combinations(arr, total, index, sequence, curr_sum)

            sequence.pop()
            curr_sum -= arr[index]
            combinations(arr, total, index + 1, sequence, curr_sum)

        combinations(candidates, target)

        return res
