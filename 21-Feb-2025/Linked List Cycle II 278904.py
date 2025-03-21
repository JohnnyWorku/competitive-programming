# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Use Floyd's algorithm

        fast = head
        slow = head
        is_there_cycle = False

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                is_there_cycle = True

            if is_there_cycle:
                fast = head

                while fast != slow:
                    fast = fast.next
                    slow = slow.next

                return fast

        