# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(curr_left, curr_right):
            if not curr_left and not curr_right:
                return True
            if not curr_left or not curr_right:
                return False

            return (curr_left.val == curr_right.val and 
                    helper(curr_left.left, curr_right.right) and 
                    helper(curr_left.right, curr_right.left))
        return helper(root.left, root.right)
        