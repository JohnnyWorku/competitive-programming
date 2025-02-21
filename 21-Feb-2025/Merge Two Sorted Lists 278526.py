# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        pointer1 = list1
        pointer2 = list2

        while pointer1 and pointer2:
            if pointer1.val <= pointer2.val:
                tail.next = pointer1
                pointer1 = pointer1.next
            else:
                tail.next = pointer2
                pointer2 = pointer2.next

            tail = tail.next

        if pointer1:
            tail.next = pointer1
        elif pointer2:
            tail.next = pointer2

        return dummy.next
            
        