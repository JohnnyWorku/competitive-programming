# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        back = None
        front = head
        if head:
            temp = head.next

        while front:
            front.next = back
            back = front
            head = front
            front = temp
            if temp:
                temp = temp.next

        return head

        