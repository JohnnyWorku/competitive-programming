# Problem:  Delete Node in a Linked List - https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # prev = node
        # nxt = node.next

        # while nxt.next:
        #     prev.val = nxt.val
        #     prev = nxt
        #     nxt = nxt.next

        # prev.val = nxt.val
        # prev.next = None

        nxt = node.next

        node.val = nxt.val
        node.next = nxt.next
        # nxt.next = None
