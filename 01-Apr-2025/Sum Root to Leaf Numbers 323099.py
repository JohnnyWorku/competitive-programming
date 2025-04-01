# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def adder(curr_node, curr_no=0):
            if not curr_node:
                return 0  # Return 0 for null nodes
            
            curr_no = (curr_no * 10) + curr_node.val
            
            # If it's a leaf node, return the computed number
            if not curr_node.left and not curr_node.right:
                return curr_no
            
            # Sum from left and right subtrees
            return adder(curr_node.left, curr_no) + adder(curr_node.right, curr_no)

        return adder(root)
        