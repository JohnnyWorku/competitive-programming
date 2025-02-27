# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

product_dict = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                product_dict[product] += 1

        res = 0
        for value in product_dict.values():
            pairs = value * (value - 1) // 2
            res += 8 * pairs

        return res