# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode()
        dummy_head.next = head
        
        prev = dummy_head
        current = head

        while current:
            temp = current.next

            if current.val == val:
                prev.next = current.next
            else:
                prev = current

            current = temp

        return dummy_head.next

        # while head and head.val == val: # being sure that head.val != val
        #     head = head.next

        # prev = head
        # if head:
        #     current = head.next
        # else:
        #     current = None

        # while current:
        #     if current.val == val:
        #         prev.next = current.next
        #     else:
        #         prev = current

        #     current = current.next

        # return head

        