# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def first_right(curr_node, curr_to_add=0):
            if not curr_node:
                return 0

            right = first_right(curr_node.right, curr_to_add)

            temp = curr_node.val
            curr_node.val += right + curr_to_add

            left = first_right(curr_node.left, temp + right + curr_to_add)

            return left + right + temp

        first_right(root)

        return root
        