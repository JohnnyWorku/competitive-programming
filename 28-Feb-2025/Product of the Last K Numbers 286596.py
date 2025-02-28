# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.stream = []
        # we define the prefix with element 1 to hanle of the initial index is 0
        self.prefix_product = [1]
        self.last_zero_index = 0

    def add(self, num: int) -> None:
        self.stream.append(num)

        if self.prefix_product[-1] != 0:
            curr_prefix_product = self.prefix_product[-1] * num
            self.prefix_product.append(curr_prefix_product)
        else:
            self.prefix_product.append(num)

        if num == 0:
            self.last_zero_index = len(self.prefix_product) - 1

    def getProduct(self, k: int) -> int:
        index = len(self.prefix_product) - k
        # If there is no 0 from index up to last element
        if self.last_zero_index < index:
            if self.prefix_product[index - 1] == 0:
                return self.prefix_product[-1]
            else:
                prefix = self.prefix_product[-1] // self.prefix_product[index - 1]
                return prefix
        else:
            return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)