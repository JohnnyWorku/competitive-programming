# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

from random import randint

class RandomizedSet:

    def __init__(self):
        self.num_dict = {}
        self.num_list = []

    def insert(self, val: int) -> bool:
        if val not in self.num_list:
            self.num_list.append(val)
            self.num_dict[val] = len(self.num_list) - 1
            return True

        return False

    def remove(self, val: int) -> bool:
        if val in self.num_dict:
            remove_index = self.num_dict[val]
            self.num_dict[self.num_list[-1]] = remove_index
            self.num_list[remove_index], self.num_list[-1] = self.num_list[-1], self.num_list[remove_index]
            del self.num_dict[self.num_list[-1]]
            self.num_list.pop()

            return True

        return False

    def getRandom(self) -> int:
        random_index = randint(0, len(self.num_list) - 1)
        return self.num_list[random_index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()