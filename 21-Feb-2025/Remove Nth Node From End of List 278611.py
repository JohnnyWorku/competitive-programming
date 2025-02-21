# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Counting its length and do their difference
        
        # dummy = ListNode()
        # dummy.next = head

        # current = head
        # size = 0

        # while current:
        #     size += 1
        #     current = current.next

        # index_to_delete = size - n
        # prev = dummy
        # current = head
        # count = 1

        # while count <= index_to_delete:
        #     prev = current
        #     current = current.next
        #     count += 1

        # prev.next = current.next

        # return dummy.next

        # Have to pointers with distance n
        dummy = ListNode()
        dummy.next = head
        faster = dummy
        slower = dummy

        for _ in range(n + 1):
            faster = faster.next

        while faster:
            faster = faster.next
            slower = slower.next

        slower.next = slower.next.next

        return dummy.next

