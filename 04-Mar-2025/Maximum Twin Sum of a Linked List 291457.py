# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # First reverse the list from the middle to the end and calculate their sum
        fast = head
        slow = head

        # Getting the middle node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow

        # Reversing
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        left = head
        right = prev
        max_sum = 0

        # Comparign sums
        while right:
            curr_sum = left.val + right.val
            max_sum = max(max_sum, curr_sum)
            right = right.next
            left = left.next

        return max_sum
        