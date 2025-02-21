# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # lst = []
        # current = head

        # while current:
        #     lst.append(current.val)
        #     current = current.next

        # left, right = 0, len(lst) - 1
        # while left <= right:
        #     if lst[left] == lst[right]:
        #         left += 1
        #         right -= 1
        #     else:
        #         return False

        # return True

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # revesing half part
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        left, right = head, prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

        