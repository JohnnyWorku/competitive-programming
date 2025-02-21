# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head

        res_dummy = ListNode()

        prev = dummy_head
        current = head
        tail = res_dummy

        while current:
            if current.val < x and current == head:
                head = head.next

            if current.val < x:
                temp = current.next
                tail.next = current
                tail = current
                current.next = None
                prev.next = temp
                current = temp
            else:
                prev = current
                current = current.next

        # to join the ramaining parts of the original list
        tail.next = head

        return res_dummy.next
        