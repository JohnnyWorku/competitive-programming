# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = Counter(nums)
        min_val = float("inf")
        max_val = -float("inf")

        for value in count_dict.values():
            min_val = min(min_val, value)
            max_val = max(max_val, value)

        buckets = [[] for _ in range(max_val - min_val + 1)]

        for key, value in count_dict.items():
            index = value - min_val
            buckets[index].append(key)

        res = []
        i = len(buckets) - 1
        is_full = False
        for _ in range(len(nums)):
            curr_bucket = buckets[i]
            for num in curr_bucket:
                if len(res) < k:
                    res.append(num)
                else:
                    return res

            i -= 1

        return res
        
