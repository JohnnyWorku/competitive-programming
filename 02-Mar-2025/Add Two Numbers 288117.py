# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        curr1 = l1
        curr2 = l2
        carry = 0

        # When both l1 and l2 are available
        while curr1 and curr2:
            curr_sum = curr1.val + curr2.val + carry
            carry = curr_sum // 10
            node_val = curr_sum % 10
            new_node = ListNode(node_val)
            tail.next = new_node
            tail = tail.next

            curr1 = curr1.next
            curr2 = curr2.next

        # When only l1 is available
        while curr1:
            curr_sum = curr1.val + carry
            carry = curr_sum // 10
            node_val = curr_sum % 10
            new_node = ListNode(node_val)
            tail.next = new_node
            tail = tail.next

            curr1 = curr1.next

        # When only l2 is available
        while curr2:
            curr_sum = curr2.val + carry
            carry = curr_sum // 10
            node_val = curr_sum % 10
            new_node = ListNode(node_val)
            tail.next = new_node
            tail = tail.next

            curr2 = curr2.next

        # If carry > 0
        if carry:
            new_node = ListNode(carry)
            tail.next = new_node
            tail = tail.next

        return dummy.next
        