# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        else:
            curr_index = 0
            current = self.dummy

            while curr_index <= index:
                current = current.next
                curr_index += 1

            return current.value

    def addAtHead(self, val: int) -> None:
        head = self.dummy.next

        new_head = Node(val)
        self.dummy.next = new_head
        new_head.next = head

        self.size += 1

        if self.size == 1:
            self.tail = new_head

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        
        if self.size == 0:
            self.addAtHead(val)
        else: 
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            curr_index = 0
            prev = self.dummy
            current = self.dummy.next

            while curr_index < index:
                prev = current
                current = current.next
                curr_index += 1

            new_node = Node(val)

            prev.next = new_node
            new_node.next = current

            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        else:
            prev = self.dummy
            current = self.dummy.next

            curr_index = 0

            while curr_index < index:
                prev = current
                current = current.next
                curr_index += 1

            print(prev, current)
            prev.next = current.next

            if index == self.size - 1:
                self.tail = prev

            self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)