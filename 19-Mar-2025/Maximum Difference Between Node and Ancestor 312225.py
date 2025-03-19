# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node, min_val, max_val):
            if not node:
                return max_val - min_val

            min_val = min(node.val, min_val)
            max_val = max(node.val, max_val)
            
            left_diff = helper(node.left, min_val, max_val)
            right_diff = helper(node.right, min_val, max_val)

            return max(left_diff, right_diff)

        return helper(root, root.val, root.val)
        