# Problem: Odd Even Linked List - https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        odd_start = head
        curr_odd = odd_start
        previous_curr_odd = curr_odd
        even_start = odd_start.next
        curr_even = even_start
        moves = 0

        while (curr_odd and curr_odd.next) or (curr_even and curr_even.next):
            if curr_odd and curr_odd.next:
                if moves < 1:
                    moves += 1
                else:
                    previous_curr_odd = curr_odd
                curr_odd.next = curr_even.next
                curr_odd = curr_even.next
            if curr_even and curr_even.next:
                curr_even.next = curr_odd.next
                curr_even = curr_odd.next

        # Joining the last node of the odds with the first node of evens
        if curr_odd:
            curr_odd.next = even_start
        elif previous_curr_odd:
            previous_curr_odd.next = even_start

        return odd_start  # It can be return head 
        