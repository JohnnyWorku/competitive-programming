# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums_dict = defaultdict(int)
        ans = []

        for num in nums:
            nums_dict[num] += 1
            if nums_dict[num] == 2:
                ans.append(num)

        return ans