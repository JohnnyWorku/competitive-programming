# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for index, char in enumerate(s):
            last_index[char] = index

        size, estimated_end = 0, 0
        res = []
        for index, char in enumerate(s):
            size += 1
            if last_index[char] > estimated_end:
                estimated_end = last_index[char]

            if index == estimated_end:
                res.append(size)
                size = 0

        return res
        