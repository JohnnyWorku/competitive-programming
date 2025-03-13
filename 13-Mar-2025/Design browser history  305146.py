# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class Node:
    def __init__(self, site=None, prev=None, next=None):
        self.site = site
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.tail = self.head
        self.candidate_tail = self.tail

    def visit(self, url: str) -> None:
        new_visit = Node(url)

        self.tail.next = new_visit
        new_visit.prev = self.tail
        self.tail = self.tail.next      

    def back(self, steps: int) -> str:
        while steps > 0 and self.tail.prev:
            self.tail = self.tail.prev
            steps -= 1

        return self.tail.site
        
    def forward(self, steps: int) -> str:
        while steps > 0 and self.tail.next:
            self.tail = self.tail.next
            steps -= 1

        return self.tail.site


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)