# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evens_sum = 0
        for num in nums:
            if num % 2 == 0:
                evens_sum += num

        evens_sum_list = []
        for query in queries:
            value, index = query
            number = nums[index]
            updated_number = number + value

            if len(evens_sum_list) > 0:
                evens_sum = evens_sum_list[-1]

            if number % 2 == 0 and updated_number % 2 == 0:
                evens_sum += value

            elif number % 2 == 1 and updated_number % 2 == 0:
                evens_sum += updated_number

            elif number % 2 == 0 and updated_number % 2 == 1:
                evens_sum -= number

            nums[index] = updated_number
            evens_sum_list.append(evens_sum)

        return evens_sum_list
