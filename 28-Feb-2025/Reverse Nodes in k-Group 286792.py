# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stopping_node = head
        prev_node_to_join = head
        next_node_to_join = head
        reversed_times = 0
        is_valid = False
        
        validity_count = 1
        while validity_count < k and stopping_node:
            stopping_node = stopping_node.next
            validity_count += 1

        if stopping_node:
            is_valid = True

        while is_valid:
            count = k
            prev = next_node_to_join
            curr = prev.next

            # We set count > 1 because it is already starting on the nodes to reverse
            while count > 1:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                count -= 1

            reversed_times += 1

            if reversed_times == 1:
                head = prev
            elif reversed_times > 1:
                prev_node_to_join.next = prev
                prev_node_to_join = next_node_to_join

            next_node_to_join = curr

            stopping_node = curr
            validity_count = 1
            while validity_count < k and stopping_node:
                stopping_node = stopping_node.next
                validity_count += 1

            if not stopping_node:
                is_valid = False

            if not is_valid:
                prev_node_to_join.next = curr

        return head
        