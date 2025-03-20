# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(path, num):
            if len(path) == k:
                res.append(path[:])
                return
            

            for candidate in range(num, n + 1):
                path.append(candidate)
                backtrack(path, candidate + 1)
                path.pop()

        backtrack([], 1)
        return res

        