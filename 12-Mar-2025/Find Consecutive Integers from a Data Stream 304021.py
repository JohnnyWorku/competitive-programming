# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.counter = 0
        self.last_element = 0

    def consec(self, num: int) -> bool:
        if self.last_element != num:
            self.counter = 0
            self.last_element = num
        
        if self.value == self.last_element:
            self.counter += 1
        
        if self.value == self.last_element and self.counter >= self.k:
            return True

        return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)