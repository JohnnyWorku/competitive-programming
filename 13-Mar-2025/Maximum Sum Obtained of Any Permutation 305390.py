# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        max_req_index = max(requests, key=lambda x: x[1])
        requests_prefix = [0] * (max_req_index[1] + 2)
        for request in requests:
            requests_prefix[request[0]] += 1
            requests_prefix[request[1] + 1] -= 1

        for i in range(1, len(requests_prefix)):
            requests_prefix[i] += requests_prefix[i - 1]

        repitition_lst = []
        for repitition in requests_prefix:
            if repitition:
                repitition_lst.append(repitition)

        nums.sort(reverse= True)
        repitition_lst.sort(reverse= True)

        res = 0
        for num, rep in zip(nums, repitition_lst):
            res += num * rep

        return res % (10 ** 9 + 7)
        